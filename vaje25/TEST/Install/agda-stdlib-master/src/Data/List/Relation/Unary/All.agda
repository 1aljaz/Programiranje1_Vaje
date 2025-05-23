------------------------------------------------------------------------
-- The Agda standard library
--
-- Lists where all elements satisfy a given property
------------------------------------------------------------------------

{-# OPTIONS --cubical-compatible --safe #-}

module Data.List.Relation.Unary.All where

open import Effect.Applicative
open import Effect.Monad
open import Data.Empty using (⊥)
open import Data.List.Base as List using (List; []; _∷_)
open import Data.List.Relation.Unary.Any as Any using (Any; here; there)
open import Data.List.Membership.Propositional renaming (_∈_ to _∈ₚ_)
import Data.List.Membership.Setoid as SetoidMembership
open import Data.Product.Base as Prod
  using (∃; -,_; _×_; _,_; proj₁; proj₂; uncurry)
open import Data.Sum.Base as Sum using (inj₁; inj₂)
open import Function.Base using (_∘_; _∘′_; id; const)
open import Level using (Level; _⊔_)
open import Relation.Nullary hiding (Irrelevant)
import Relation.Nullary.Decidable as Dec
open import Relation.Unary hiding (_∈_)
open import Relation.Binary using (Setoid; _Respects_)
open import Relation.Binary.PropositionalEquality.Core as P
import Relation.Binary.PropositionalEquality.Properties as P

private
  variable
    a b p q r ℓ : Level
    A : Set a
    B : Set b
    P Q R : Pred A p
    x : A
    xs : List A

------------------------------------------------------------------------
-- Definitions

-- Given a predicate P, then All P xs means that every element in xs
-- satisfies P. See `Relation.Unary` for an explanation of predicates.

infixr 5 _∷_

data All {A : Set a} (P : Pred A p) : Pred (List A) (a ⊔ p) where
  []  : All P []
  _∷_ : ∀ {x xs} (px : P x) (pxs : All P xs) → All P (x ∷ xs)

-- All P xs is a finite map from indices x ∈ xs to content P x.
-- Relation pxs [ i ]= px states that, in map pxs, key i : x ∈ xs points to value px.

infix 4 _[_]=_

data _[_]=_ {A : Set a} {P : Pred A p} :
            ∀ {x xs} → All P xs → x ∈ₚ xs → P x → Set (a ⊔ p) where

  here  : ∀ {x xs} {px : P x} {pxs : All P xs} →
          px ∷ pxs [ here refl ]= px

  there : ∀ {x xs y} {px : P x} {pxs : All P xs} {py : P y} {i : x ∈ₚ xs} →
          pxs [ i ]= px →
          py ∷ pxs [ there i ]= px

-- A list is empty if having an element is impossible.

Null : Pred (List A) _
Null = All (λ _ → ⊥)

------------------------------------------------------------------------
-- Operations on All

uncons : All P (x ∷ xs) → P x × All P xs
uncons (px ∷ pxs) = px , pxs

head : All P (x ∷ xs) → P x
head = proj₁ ∘ uncons

tail : All P (x ∷ xs) → All P xs
tail = proj₂ ∘ uncons

reduce : (f : ∀ {x} → P x → B) → All P xs → List B
reduce f []         = []
reduce f (px ∷ pxs) = f px ∷ reduce f pxs

construct : (f : B → ∃ P) (xs : List B) → ∃ (All P)
construct f []       = [] , []
construct f (x ∷ xs) = Prod.zip _∷_ _∷_ (f x) (construct f xs)

fromList : (xs : List (∃ P)) → All P (List.map proj₁ xs)
fromList []              = []
fromList ((x , p) ∷ xps) = p ∷ fromList xps

toList : All P xs → List (∃ P)
toList pxs = reduce (λ {x} px → x , px) pxs

map : P ⊆ Q → All P ⊆ All Q
map g []         = []
map g (px ∷ pxs) = g px ∷ map g pxs

zipWith : P ∩ Q ⊆ R → All P ∩ All Q ⊆ All R
zipWith f ([] , [])             = []
zipWith f (px ∷ pxs , qx ∷ qxs) = f (px , qx) ∷ zipWith f (pxs , qxs)

unzipWith : R ⊆ P ∩ Q → All R ⊆ All P ∩ All Q
unzipWith f []         = [] , []
unzipWith f (rx ∷ rxs) = Prod.zip _∷_ _∷_ (f rx) (unzipWith f rxs)

zip : All P ∩ All Q ⊆ All (P ∩ Q)
zip = zipWith id

unzip : All (P ∩ Q) ⊆ All P ∩ All Q
unzip = unzipWith id

module _(S : Setoid a ℓ) {P : Pred (Setoid.Carrier S) p} where
  open Setoid S renaming (Carrier to C; refl to refl₁)
  open SetoidMembership S

  tabulateₛ : (∀ {x} → x ∈ xs → P x) → All P xs
  tabulateₛ {[]}     hyp = []
  tabulateₛ {x ∷ xs} hyp = hyp (here refl₁) ∷ tabulateₛ (hyp ∘ there)

tabulate : (∀ {x} → x ∈ₚ xs → P x) → All P xs
tabulate = tabulateₛ (P.setoid _)

self : ∀ {xs : List A} → All (const A) xs
self = tabulate (λ {x} _ → x)

------------------------------------------------------------------------
-- (weak) updateAt

infixl 6 _[_]%=_ _[_]≔_

updateAt : x ∈ₚ xs → (P x → P x) → All P xs → All P xs
updateAt () f []
updateAt (here refl) f (px ∷ pxs) = f px ∷ pxs
updateAt (there i)   f (px ∷ pxs) =   px ∷ updateAt i f pxs

_[_]%=_ : All P xs → x ∈ₚ xs → (P x → P x) → All P xs
pxs [ i ]%= f = updateAt i f pxs

_[_]≔_ : All P xs → x ∈ₚ xs → P x → All P xs
pxs [ i ]≔ px = pxs [ i ]%= const px

------------------------------------------------------------------------
-- Traversable-like functions

module _ (p : Level) {A : Set a} {P : Pred A (a ⊔ p)}
         {F : Set (a ⊔ p) → Set (a ⊔ p)}
         (App : RawApplicative F)
         where

  open RawApplicative App

  sequenceA : All (F ∘′ P) ⊆ F ∘′ All P
  sequenceA []       = pure []
  sequenceA (x ∷ xs) = _∷_ <$> x <*> sequenceA xs

  mapA : ∀ {Q : Pred A q} → (Q ⊆ F ∘′ P) → All Q ⊆ (F ∘′ All P)
  mapA f = sequenceA ∘′ map f

  forA : ∀ {Q : Pred A q} → All Q xs → (Q ⊆ F ∘′ P) → F (All P xs)
  forA qxs f = mapA f qxs

module _ (p : Level) {A : Set a} {P : Pred A (a ⊔ p)}
         {M : Set (a ⊔ p) → Set (a ⊔ p)}
         (Mon : RawMonad M)
         where

  private App = RawMonad.rawApplicative Mon

  sequenceM : All (M ∘′ P) ⊆ M ∘′ All P
  sequenceM = sequenceA p App

  mapM : ∀ {Q : Pred A q} → (Q ⊆ M ∘′ P) → All Q ⊆ (M ∘′ All P)
  mapM = mapA p App

  forM : ∀ {Q : Pred A q} → All Q xs → (Q ⊆ M ∘′ P) → M (All P xs)
  forM = forA p App

------------------------------------------------------------------------
-- Generalised lookup based on a proof of Any

lookupAny : All P xs → (i : Any Q xs) → (P ∩ Q) (Any.lookup i)
lookupAny (px ∷ pxs) (here qx) = px , qx
lookupAny (px ∷ pxs) (there i) = lookupAny pxs i

lookupWith : ∀[ P ⇒ Q ⇒ R ] → All P xs → (i : Any Q xs) → R (Any.lookup i)
lookupWith f pxs i = Prod.uncurry f (lookupAny pxs i)

lookup : All P xs → (∀ {x} → x ∈ₚ xs → P x)
lookup pxs = lookupWith (λ { px refl → px }) pxs

module _(S : Setoid a ℓ) {P : Pred (Setoid.Carrier S) p} where
  open Setoid S renaming (sym to sym₁)
  open SetoidMembership S

  lookupₛ : P Respects _≈_ → All P xs → (∀ {x} → x ∈ xs → P x)
  lookupₛ resp pxs = lookupWith (λ py x=y → resp (sym₁ x=y) py) pxs

------------------------------------------------------------------------
-- Properties of predicates preserved by All

all? : Decidable P → Decidable (All P)
all? p []       = yes []
all? p (x ∷ xs) = Dec.map′ (uncurry _∷_) uncons (p x ×-dec all? p xs)

universal : Universal P → Universal (All P)
universal u []       = []
universal u (x ∷ xs) = u x ∷ universal u xs

irrelevant : Irrelevant P → Irrelevant (All P)
irrelevant irr []           []           = P.refl
irrelevant irr (px₁ ∷ pxs₁) (px₂ ∷ pxs₂) =
  P.cong₂ _∷_ (irr px₁ px₂) (irrelevant irr pxs₁ pxs₂)

satisfiable : Satisfiable (All P)
satisfiable = [] , []

------------------------------------------------------------------------
-- Generalised decidability procedure

decide :  Π[ P ∪ Q ] → Π[ All P ∪ Any Q ]
decide p∪q [] = inj₁ []
decide p∪q (x ∷ xs) with p∪q x
... | inj₂ qx = inj₂ (here qx)
... | inj₁ px = Sum.map (px ∷_) there (decide p∪q xs)

------------------------------------------------------------------------
-- DEPRECATED
------------------------------------------------------------------------
-- Please use the new names as continuing support for the old names is
-- not guaranteed.

-- Version 1.4

all = all?
{-# WARNING_ON_USAGE all
"Warning: all was deprecated in v1.4.
Please use all? instead."
#-}
