# BCG structured dataset — research draft

Version: bcg-evidence-v2 · assembled 27 October 2026 · 14 evidence records · 14 linked sources.

**Not independently clinically reviewed, exhaustive, or complete for personal vaccination decisions.** The JSON separates published estimates, derived relative effects, unavailable clinical outputs, and an explicitly assumption-based research model.

## Principal inputs

| Input | Value | Scope |
|---|---|---|
| Prevalence | 236.14 per 100,000 (95% UI 214.51–260.20) | Global 2021 age-standardised modelled TB prevalence, Jiang et al. |
| Disability weight | 0.333 on a 0–1 scale | WHO reference for the symptomatic TB health state without HIV infection; not mortality risk |
| Death during treatment | 19.3% (95% CI 14.0–26.1) | Historical childhood TB-meningitis cohorts; not all TB |
| Neurological sequelae | 53.9% (95% CI 42.6–64.9) | Survivors of childhood TB meningitis; a different denominator |
| Incidence | 131 per 100,000 (uncertainty interval 122–141) | WHO global 2024 incidence, separate from 2021 prevalence |

The four earlier benefit/safety domains remain: infant trial rate ratios for pulmonary and meningeal/miliary TB; an adjusted odds ratio for TB in under-five contacts; qualitative expected local reactions; and product-specific AJV safety frequency bands. Every numerical record states its population, outcome, comparison, period, measure, source IDs and limitations.

## What the research calculation means

`(236.14 / 100000) × 0.333 = 0.0007863462`

Displayed as **0.07863462 per 100 index points**, rounded to **0.079**, equivalently **78.63462 weighted index units per 100,000**.

This is an illustrative morbidity calculation using sourced inputs. It is **not** a 0.079% chance of illness, death or vaccine harm, and is not a reproduction of an official WHO/GBD burden estimate.

The model assumes the symptomatic, HIV-negative health-state weight can be applied uniformly to the reported prevalence. Symptom distribution, case-definition and HIV-scope compatibility have not been independently audited. It excludes premature mortality, additional post-TB effects, personal risk and vaccine-attributable benefits/harms. No joint uncertainty interval has been estimated. Do not rank total disease or vaccine risk using this proxy alone.

Age-standardisation adjusts rates to a reference age profile. It does not give the actual prevalence in the current population or the risk for the age entered on the website. Region, age and sex do not personalise this global reference. Global incidence is not an unvaccinated baseline; the 2024 map is not an input to the 2021 research calculation.

## Evidence conventions

- `null` means unavailable/not assessed, never zero.
- Infant relative rate reductions are calculated as `100 × (1 − rate ratio)`; confidence bounds are reversed.
- The cohort adjusted odds ratio remains an odds ratio, not a percentage reduction in risk.
- AJV frequency bands have an excluded upper bound; they are not confidence intervals, excess risks, or universal BCG product rates. The label does not give a common observation window.
- Childhood death and sequelae percentages have different denominators. They are not added together or multiplied into the global prevalence.
- Background source checking is not independent clinical validation. Gaps include subgroup matching, full trial disclosure/exclusion appraisal, review of current evidence completeness, and a validated clinical risk model.

## Sources

- [WHO — Global tuberculosis report 2025, section 1.1](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/tb-disease-burden/1-1-tb-incidence) — publication/revision: 2025; checked 2026-10-27. Locate: Opening paragraph and Table 1.1.1, Global row.
- [Mangtani et al. — Protection by BCG vaccine against tuberculosis](https://doi.org/10.1093/cid/cit790) — publication/revision: 2014; checked 2026-10-27. Locate: Abstract, Results; infant subgroups.
- [Martinez et al. — Infant BCG vaccination throughout the life course](https://stacks.cdc.gov/view/cdc/131794) — publication/revision: 2022; checked 2026-10-27. Locate: Abstract, Findings; children younger than 5 years.
- [BCG Vaccine AJV — UK product information](https://www.medicines.org.uk/emc/product/9890/smpc) — publication/revision: 2023-10-19; checked 2026-10-27. Locate: Sections 4.3, 4.8 and 10.
- [WHO — BCG vaccine reaction information sheet](https://cdn.who.int/media/docs/default-source/pvg/global-vaccine-safety/bcg-vaccine-rates-information-sheet.pdf) — publication/revision: 2012-04; checked 2026-10-27. Locate: Page 1, Mild adverse events; page 2, systemic adverse events.
- [WHO — BCG vaccines position paper](https://www.who.int/publications/i/item/who-wer9308-73-96) — publication/revision: 2018-02-23; checked 2026-10-27. Locate: Position paper and accompanying recommendations.
- [WHO — Tuberculosis fact sheet](https://www.who.int/news-room/fact-sheets/detail/tuberculosis) — publication/revision: not recorded; checked 2026-10-27. Locate: Overview, symptoms and prevention.
- [CDC — Tuberculosis vaccine](https://www.cdc.gov/tb/vaccines/index.html) — publication/revision: not recorded; checked 2026-10-27. Locate: BCG vaccine overview.
- [Jiang et al. — Global TB burden, 1990–2050 (GBD 2021 analysis)](https://doi.org/10.1097/JS9.0000000000003412) — publication/revision: 2026-01; checked 2026-10-27. Locate: Results: Age-standardized annual rate of four basic indicators; global 2021 prevalence.
- [WHO — Global burden of disease methods 2000–2021](https://cdn.who.int/media/docs/default-source/gho-documents/global-health-estimates/ghe2021_daly_methods.pdf?sfvrsn=690b16c3_2) — publication/revision: 2024-05; checked 2026-10-27. Locate: Section 2.4 prevalence-based YLDs; Annex Table C, Tuberculosis, not HIV infected.
- [Chiang et al. — Treatment outcomes of childhood tuberculous meningitis](https://doi.org/10.1016/S1473-3099(14)70852-7) — publication/revision: 2014-10; checked 2026-10-27. Locate: Abstract, Findings; 19 studies, 1,636 children.

## Data and implementation

The canonical file is `dist/data/bcg.json` in the Sites development layout, or `data/bcg.json` in the GitHub Pages root layout. The page fetches static JSON and has an identical embedded fallback for offline use. There is no database, personal-data API or account system. The original WHO map image needs internet access; its numerical categories remain unchanged while a native frontend filter applies green for lower incidence and red for higher incidence. The adaptation is labelled and is not endorsed by WHO.

After editing the canonical JSON, run:

```sh
python3 scripts/embed-bcg.py
python3 scripts/validate-bcg.py
```

The scripts detect either layout. Validation checks source-reference completeness, numerical interval bounds, derived-effect arithmetic, model arithmetic, explicit assumption flags and matching offline data. It does not validate the clinical appropriateness of the model.

## 27 October interface and context update

Added WHO 2024 adult male, adult female and child case-count records with uncertainty intervals, plus linked CDC common-cold, WHO Ebola and EMA benefit–risk references. The AGE and SEX boxes distinguish disease burden from vaccine subgroup effects; they do not apply unsupported age/sex multipliers.

The common-cold and Ebola rows are contextual comparisons only. Their numerical morbidity-index fields remain null because matched prevalence and disability-weight inputs are missing. Ebola case fatality and annual cold episode counts are not compatible substitutes for the index inputs. Relative-reduction examples use explicitly hypothetical rates, not clinical forecasts.

The final balance uses an effects-table approach, including denominator, period, severity, uncertainty and missing inputs. No net benefit, suitability score or recommendation is calculated. Source metadata and the original research-model limitations remain in the JSON and expandable methods. The map is placed first in the regional prevalence box and explicitly labelled as incidence; the separate numeric prevalence remains a global age-standardised 2021 reference.
