------------------------------------------------------------------------
-- The Agda standard library
--
-- Consequences of a monomorphism between ring-like structures
------------------------------------------------------------------------

-- See Data.Nat.Binary.Properties for examples of how this and similar
-- modules can be used to easily translate properties between types.

{-# OPTIONS --cubical-compatible --safe #-}

open import Algebra.Bundles
open import Algebra.Morphism.Structures
import Algebra.Morphism.GroupMonomorphism  as GroupMonomorphism
import Algebra.Morphism.MonoidMonomorphism as MonoidMonomorphism
open import Relation.Binary.Core

module Algebra.Morphism.RingMonomorphism
  {a b ℓ₁ ℓ₂} {R₁ : RawRing a ℓ₁} {R₂ : RawRing b ℓ₂} {⟦_⟧}
  (isRingMonomorphism : IsRingMonomorphism R₁ R₂ ⟦_⟧)
  where

open IsRingMonomorphism isRingMonomorphism
open RawRing R₁ renaming (Carrier to A; _≈_ to _≈₁_)
open RawRing R₂ renaming
  ( Carrier to B; _≈_ to _≈₂_; _+_ to _⊕_
  ; _*_ to _⊛_; 1# to 1#₂; 0# to 0#₂; -_ to ⊝_)

open import Algebra.Definitions
open import Algebra.Structures
open import Data.Product
import Relation.Binary.Reasoning.Setoid as SetoidReasoning

------------------------------------------------------------------------
-- Re-export all properties of group and monoid monomorphisms

open GroupMonomorphism +-isGroupMonomorphism public
  renaming
  ( assoc   to +-assoc
  ; comm    to +-comm
  ; cong    to +-cong
  ; idem    to +-idem
  ; sel     to +-sel
  ; ⁻¹-cong to neg-cong

  ; identity to +-identity; identityˡ to +-identityˡ; identityʳ to +-identityʳ
  ; cancel   to +-cancel;   cancelˡ   to +-cancelˡ;   cancelʳ   to +-cancelʳ
  ; zero     to +-zero;     zeroˡ     to +-zeroˡ;     zeroʳ     to +-zeroʳ

  ; isMagma             to +-isMagma
  ; isSemigroup         to +-isSemigroup
  ; isMonoid            to +-isMonoid
  ; isSelectiveMagma    to +-isSelectiveMagma
  ; isBand              to +-isBand
  ; isCommutativeMonoid to +-isCommutativeMonoid
  )

open MonoidMonomorphism *-isMonoidMonomorphism public
  renaming
  ( assoc to *-assoc
  ; comm  to *-comm
  ; cong  to *-cong
  ; idem  to *-idem
  ; sel   to *-sel

  ; identity to *-identity; identityˡ to *-identityˡ; identityʳ to *-identityʳ
  ; cancel   to *-cancel;   cancelˡ   to *-cancelˡ;   cancelʳ   to *-cancelʳ
  ; zero     to *-zero;     zeroˡ     to *-zeroˡ;     zeroʳ     to *-zeroʳ

  ; isMagma             to *-isMagma
  ; isSemigroup         to *-isSemigroup
  ; isMonoid            to *-isMonoid
  ; isSelectiveMagma    to *-isSelectiveMagma
  ; isBand              to *-isBand
  ; isCommutativeMonoid to *-isCommutativeMonoid
  )

------------------------------------------------------------------------
-- Properties

module _ (+-isGroup : IsGroup _≈₂_ _⊕_ 0#₂ ⊝_)
         (*-isMagma : IsMagma _≈₂_ _⊛_) where

  open IsGroup +-isGroup hiding (setoid; refl; sym)
  open IsMagma *-isMagma renaming (∙-cong to ◦-cong)
  open SetoidReasoning setoid

  distribˡ : _DistributesOverˡ_ _≈₂_ _⊛_ _⊕_ → _DistributesOverˡ_ _≈₁_ _*_ _+_
  distribˡ distribˡ x y z = injective (begin
    ⟦ x * (y + z) ⟧               ≈⟨ *-homo x (y + z) ⟩
    ⟦ x ⟧ ⊛ ⟦ y + z ⟧             ≈⟨ ◦-cong refl (+-homo y z) ⟩
    ⟦ x ⟧ ⊛ (⟦ y ⟧ ⊕ ⟦ z ⟧)       ≈⟨ distribˡ ⟦ x ⟧ ⟦ y ⟧ ⟦ z ⟧ ⟩
    ⟦ x ⟧ ⊛ ⟦ y ⟧ ⊕ ⟦ x ⟧ ⊛ ⟦ z ⟧ ≈˘⟨ ∙-cong (*-homo x y) (*-homo x z) ⟩
    ⟦ x * y ⟧ ⊕ ⟦ x * z ⟧         ≈˘⟨ +-homo (x * y) (x * z) ⟩
    ⟦ x * y + x * z ⟧ ∎)

  distribʳ : _DistributesOverʳ_ _≈₂_ _⊛_ _⊕_ → _DistributesOverʳ_ _≈₁_ _*_ _+_
  distribʳ distribˡ x y z = injective (begin
    ⟦ (y + z) * x ⟧               ≈⟨ *-homo (y + z) x ⟩
    ⟦ y + z ⟧ ⊛ ⟦ x ⟧             ≈⟨ ◦-cong (+-homo y z) refl ⟩
    (⟦ y ⟧ ⊕ ⟦ z ⟧) ⊛ ⟦ x ⟧       ≈⟨ distribˡ ⟦ x ⟧ ⟦ y ⟧ ⟦ z ⟧ ⟩
    ⟦ y ⟧ ⊛ ⟦ x ⟧ ⊕ ⟦ z ⟧ ⊛ ⟦ x ⟧ ≈˘⟨ ∙-cong (*-homo y x) (*-homo z x) ⟩
    ⟦ y * x ⟧ ⊕ ⟦ z * x ⟧         ≈˘⟨ +-homo (y * x) (z * x) ⟩
    ⟦ y * x + z * x ⟧ ∎)

  distrib : _DistributesOver_ _≈₂_ _⊛_ _⊕_ → _DistributesOver_ _≈₁_ _*_ _+_
  distrib distrib = distribˡ (proj₁ distrib) , distribʳ (proj₂ distrib)

  zeroˡ : LeftZero _≈₂_ 0#₂ _⊛_ → LeftZero _≈₁_ 0# _*_
  zeroˡ zeroˡ x = injective (begin
    ⟦ 0# * x ⟧     ≈⟨ *-homo 0# x ⟩
    ⟦ 0# ⟧ ⊛ ⟦ x ⟧ ≈⟨ ◦-cong 0#-homo refl ⟩
    0#₂ ⊛ ⟦ x ⟧    ≈⟨ zeroˡ ⟦ x ⟧ ⟩
    0#₂            ≈˘⟨ 0#-homo ⟩
    ⟦ 0# ⟧         ∎)

  zeroʳ : RightZero _≈₂_ 0#₂ _⊛_ → RightZero _≈₁_ 0# _*_
  zeroʳ zeroʳ x = injective (begin
    ⟦ x * 0# ⟧     ≈⟨ *-homo x 0# ⟩
    ⟦ x ⟧ ⊛ ⟦ 0# ⟧ ≈⟨ ◦-cong refl 0#-homo ⟩
    ⟦ x ⟧ ⊛ 0#₂    ≈⟨ zeroʳ ⟦ x ⟧ ⟩
    0#₂            ≈˘⟨ 0#-homo ⟩
    ⟦ 0# ⟧         ∎)

  zero : Zero _≈₂_ 0#₂ _⊛_ → Zero _≈₁_ 0# _*_
  zero zero = zeroˡ (proj₁ zero) , zeroʳ (proj₂ zero)

  neg-distribˡ-* : (∀ x y → (⊝ (x ⊛ y)) ≈₂ ((⊝ x) ⊛ y)) → (∀ x y → (- (x * y)) ≈₁ ((- x) * y))
  neg-distribˡ-* neg-distribˡ-* x y = injective (begin
    ⟦ - (x * y) ⟧     ≈⟨ -‿homo (x * y) ⟩
    ⊝ ⟦ x * y ⟧       ≈⟨ ⁻¹-cong (*-homo x y) ⟩
    ⊝ (⟦ x ⟧ ⊛ ⟦ y ⟧) ≈⟨ neg-distribˡ-* ⟦ x ⟧ ⟦ y ⟧ ⟩
    ⊝ ⟦ x ⟧ ⊛ ⟦ y ⟧   ≈⟨ ◦-cong (sym (-‿homo x)) refl ⟩
    ⟦ - x ⟧ ⊛ ⟦ y ⟧   ≈⟨ sym (*-homo (- x) y) ⟩
    ⟦ - x * y ⟧       ∎)

  neg-distribʳ-* : (∀ x y → (⊝ (x ⊛ y)) ≈₂ (x ⊛ (⊝ y))) → (∀ x y → (- (x * y)) ≈₁ (x * (- y)))
  neg-distribʳ-* neg-distribʳ-* x y = injective (begin
    ⟦ - (x * y) ⟧     ≈⟨ -‿homo (x * y) ⟩
    ⊝ ⟦ x * y ⟧       ≈⟨ ⁻¹-cong (*-homo x y) ⟩
    ⊝ (⟦ x ⟧ ⊛ ⟦ y ⟧) ≈⟨ neg-distribʳ-* ⟦ x ⟧ ⟦ y ⟧ ⟩
    ⟦ x ⟧ ⊛ ⊝ ⟦ y ⟧   ≈⟨ ◦-cong refl (sym (-‿homo y)) ⟩
    ⟦ x ⟧ ⊛ ⟦ - y ⟧   ≈⟨ sym (*-homo x (- y)) ⟩
    ⟦ x * - y ⟧       ∎)

isRing : IsRing _≈₂_ _⊕_ _⊛_ ⊝_ 0#₂ 1#₂ → IsRing _≈₁_ _+_ _*_ -_ 0# 1#
isRing isRing = record
  { +-isAbelianGroup = isAbelianGroup R.+-isAbelianGroup
  ; *-cong           = *-cong R.*-isMagma
  ; *-assoc          = *-assoc R.*-isMagma R.*-assoc
  ; *-identity       = *-identity R.*-isMagma R.*-identity
  ; distrib          = distrib R.+-isGroup R.*-isMagma R.distrib
  ; zero             = zero R.+-isGroup R.*-isMagma R.zero
  } where module R = IsRing isRing

isCommutativeRing : IsCommutativeRing _≈₂_ _⊕_ _⊛_ ⊝_ 0#₂ 1#₂ →
                    IsCommutativeRing _≈₁_ _+_ _*_ -_ 0# 1#
isCommutativeRing isCommRing = record
  { isRing = isRing C.isRing
  ; *-comm = *-comm C.*-isMagma C.*-comm
  } where module C = IsCommutativeRing isCommRing
