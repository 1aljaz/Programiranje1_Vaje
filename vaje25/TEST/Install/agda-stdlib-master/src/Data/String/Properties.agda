------------------------------------------------------------------------
-- The Agda standard library
--
-- Properties of operations on strings
------------------------------------------------------------------------

{-# OPTIONS --cubical-compatible --safe #-}

module Data.String.Properties where

open import Data.Bool.Base using (Bool)
import Data.Char.Properties as Charₚ
import Data.List.Properties as Listₚ
import Data.List.Relation.Binary.Pointwise as Pointwise
import Data.List.Relation.Binary.Lex.Strict as StrictLex
open import Data.String.Base
open import Function.Base
open import Relation.Nullary.Decidable using (yes; no)
open import Relation.Nullary.Decidable using (map′; isYes)
open import Relation.Binary
open import Relation.Binary.PropositionalEquality.Core
import Relation.Binary.Construct.On as On
import Relation.Binary.PropositionalEquality.Properties as PropEq

------------------------------------------------------------------------
-- Primitive properties

open import Agda.Builtin.String.Properties public
  renaming ( primStringToListInjective to toList-injective)

------------------------------------------------------------------------
-- Properties of _≈_

≈⇒≡ : _≈_ ⇒ _≡_
≈⇒≡ = toList-injective _ _
    ∘ Pointwise.Pointwise-≡⇒≡

≈-reflexive : _≡_ ⇒ _≈_
≈-reflexive = Pointwise.≡⇒Pointwise-≡
            ∘ cong toList

≈-refl : Reflexive _≈_
≈-refl {x} = ≈-reflexive {x} {x} refl

≈-sym : Symmetric _≈_
≈-sym = Pointwise.symmetric sym

≈-trans : Transitive _≈_
≈-trans = Pointwise.transitive trans

≈-subst : ∀ {ℓ} → Substitutive _≈_ ℓ
≈-subst P x≈y p = subst P (≈⇒≡ x≈y) p

infix 4 _≈?_
_≈?_ : Decidable _≈_
x ≈? y = Pointwise.decidable Charₚ._≟_ (toList x) (toList y)

≈-isEquivalence : IsEquivalence _≈_
≈-isEquivalence = record
  { refl  = λ {i} → ≈-refl {i}
  ; sym   = λ {i j} → ≈-sym {i} {j}
  ; trans = λ {i j k} → ≈-trans {i} {j} {k}
  }

≈-setoid : Setoid _ _
≈-setoid = record
  { isEquivalence = ≈-isEquivalence
  }

≈-isDecEquivalence : IsDecEquivalence _≈_
≈-isDecEquivalence = record
  { isEquivalence = ≈-isEquivalence
  ; _≟_           = _≈?_
  }

≈-decSetoid : DecSetoid _ _
≈-decSetoid = record
  { isDecEquivalence = ≈-isDecEquivalence
  }

-----------------------------------------------------------------------
-- Properties of _≡_

infix 4 _≟_

_≟_ : Decidable _≡_
x ≟ y = map′ ≈⇒≡ ≈-reflexive $ x ≈? y

≡-setoid : Setoid _ _
≡-setoid = PropEq.setoid String

≡-decSetoid : DecSetoid _ _
≡-decSetoid = PropEq.decSetoid _≟_

------------------------------------------------------------------------
-- Properties of _<_

infix 4 _<?_
_<?_ : Decidable _<_
x <? y = StrictLex.<-decidable Charₚ._≟_ Charₚ._<?_ (toList x) (toList y)

<-isStrictPartialOrder-≈ : IsStrictPartialOrder _≈_ _<_
<-isStrictPartialOrder-≈ =
  On.isStrictPartialOrder
    toList
    (StrictLex.<-isStrictPartialOrder Charₚ.<-isStrictPartialOrder)

<-isStrictTotalOrder-≈ : IsStrictTotalOrder _≈_ _<_
<-isStrictTotalOrder-≈ =
  On.isStrictTotalOrder
    toList
    (StrictLex.<-isStrictTotalOrder Charₚ.<-isStrictTotalOrder)

<-strictPartialOrder-≈ : StrictPartialOrder _ _ _
<-strictPartialOrder-≈ =
  On.strictPartialOrder
    (StrictLex.<-strictPartialOrder Charₚ.<-strictPartialOrder)
    toList

<-strictTotalOrder-≈ : StrictTotalOrder _ _ _
<-strictTotalOrder-≈ =
  On.strictTotalOrder
    (StrictLex.<-strictTotalOrder Charₚ.<-strictTotalOrder)
    toList

≤-isDecPartialOrder-≈ : IsDecPartialOrder _≈_ _≤_
≤-isDecPartialOrder-≈ =
  On.isDecPartialOrder
    toList
    (StrictLex.≤-isDecPartialOrder Charₚ.<-isStrictTotalOrder)

≤-isDecTotalOrder-≈ : IsDecTotalOrder _≈_ _≤_
≤-isDecTotalOrder-≈ =
  On.isDecTotalOrder
    toList
    (StrictLex.≤-isDecTotalOrder Charₚ.<-isStrictTotalOrder)

≤-decTotalOrder-≈ :  DecTotalOrder _ _ _
≤-decTotalOrder-≈ =
  On.decTotalOrder
    (StrictLex.≤-decTotalOrder Charₚ.<-strictTotalOrder)
    toList

≤-decPoset-≈ : DecPoset _ _ _
≤-decPoset-≈ =
  On.decPoset
    (StrictLex.≤-decPoset Charₚ.<-strictTotalOrder)
    toList

------------------------------------------------------------------------
-- Alternative Boolean equality test.
--
-- Why is the definition _==_ = primStringEquality not used? One
-- reason is that the present definition can sometimes improve type
-- inference, at least with the version of Agda that is current at the
-- time of writing: see unit-test below.

infix 4 _==_
_==_ : String → String → Bool
s₁ == s₂ = isYes (s₁ ≟ s₂)

private

  -- The following unit test does not type-check (at the time of
  -- writing) if _==_ is replaced by primStringEquality.

  data P : (String → Bool) → Set where
    p : (c : String) → P (_==_ c)

  unit-test : P (_==_ "")
  unit-test = p _
