**daftar nama-nama function**, **dikelompokkan berdasarkan jenisnya** (single-objective, constrained, dan multi-objective), **serta penjelasan apakah domain-nya standar atau tidak.**

---

## 🧩 **Test Functions for Single-Objective Optimization**

| No | Function Name    | Domain                   | Domain Standar?   |
| -- | ---------------- | ------------------------ | ----------------- |
| 1  | Rastrigin        | −5.12 ≤ xᵢ ≤ 5.12        | ✅ Ya              |
| 2  | Ackley           | −5 ≤ x, y ≤ 5            | ✅ Ya              |
| 3  | Sphere           | −∞ ≤ xᵢ ≤ ∞              | ⚠️ Tidak terbatas |
| 4  | Rosenbrock       | −∞ ≤ xᵢ ≤ ∞              | ⚠️ Tidak terbatas |
| 5  | Beale            | −4.5 ≤ x, y ≤ 4.5        | ✅ Ya              |
| 6  | Goldstein–Price  | −2 ≤ x, y ≤ 2            | ✅ Ya              |
| 7  | Booth            | −10 ≤ x, y ≤ 10          | ✅ Ya              |
| 8  | Bukin N.6        | −15 ≤ x ≤ −5, −3 ≤ y ≤ 3 | ✅ Ya              |
| 9  | Matyas           | −10 ≤ x, y ≤ 10          | ✅ Ya              |
| 10 | Lévi N.13        | −10 ≤ x, y ≤ 10          | ✅ Ya              |
| 11 | Griewank         | −∞ ≤ xᵢ ≤ ∞              | ⚠️ Tidak terbatas |
| 12 | Himmelblau       | −5 ≤ x, y ≤ 5            | ✅ Ya              |
| 13 | Three-hump camel | −5 ≤ x, y ≤ 5            | ✅ Ya              |
| 14 | Easom            | −100 ≤ x, y ≤ 100        | ✅ Ya              |
| 15 | Cross-in-tray    | −10 ≤ x, y ≤ 10          | ✅ Ya              |
| 16 | Eggholder        | −512 ≤ x, y ≤ 512        | ✅ Ya              |
| 17 | Hölder table     | −10 ≤ x, y ≤ 10          | ✅ Ya              |
| 18 | McCormick        | −1.5 ≤ x ≤ 4, −3 ≤ y ≤ 4 | ✅ Ya              |
| 19 | Schaffer N.2     | −100 ≤ x, y ≤ 100        | ✅ Ya              |
| 20 | Schaffer N.4     | −100 ≤ x, y ≤ 100        | ✅ Ya              |
| 21 | Styblinski–Tang  | −5 ≤ xᵢ ≤ 5              | ✅ Ya              |
| 22 | Shekel           | −∞ ≤ xᵢ ≤ ∞              | ⚠️ Tidak terbatas |

**➡ Kesimpulan:**

* ✅ Domain standar (terbatas): **18 fungsi**
* ⚠️ Domain tidak terbatas (−∞ ≤ x ≤ ∞): **4 fungsi**
  → *Sphere, Rosenbrock, Griewank, Shekel*

---

## ⚙️ **Test Functions for Constrained Optimization**

| No | Function Name                      | Domain                            | Domain Standar? |
| -- | ---------------------------------- | --------------------------------- | --------------- |
| 1  | Rosenbrock (constrained to a disk) | −1.5 ≤ x, y ≤ 1.5                 | ✅ Ya            |
| 2  | Mishra’s Bird (constrained)        | −10 ≤ x ≤ 0, −6.5 ≤ y ≤ 0         | ✅ Ya            |
| 3  | Townsend (modified)                | −2.25 ≤ x ≤ 2.25, −2.5 ≤ y ≤ 1.75 | ✅ Ya            |
| 4  | Keane’s bump                       | 0 < xᵢ < 10                       | ✅ Ya            |

**➡ Semua domain constrained ini adalah domain terbatas → ✅ Standar**

---

## 🎯 **Test Functions for Multi-Objective Optimization**

| No | Function Name | Domain                  | Domain Standar?    |
| -- | ------------- | ----------------------- | ------------------ |
| 1  | Binh and Korn | (tidak ditulis di teks) | ⚠️ Tidak diketahui |

---

### 🔍 **Rekap Keseluruhan**

* **Total function (single + constrained):** 26
* **Domain standar (terbatas):** 22
* **Domain tidak terbatas:** 4 (Sphere, Rosenbrock, Griewank, Shekel)
* **Multi-objective (Binh & Korn):** domain tidak disebutkan.

---
