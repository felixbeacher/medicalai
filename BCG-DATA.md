# BCG evidence dataset

Canonical data: `dist/data/bcg.json`. The site fetches this static JSON when hosted; the identical embedded snapshot supports offline HTML use. There is no database, account system or medical API. Source links are in each estimate and in the page's BCG source register.

## Scope and status

Selected evidence, source-checked on 27 October 2026. **Not independently clinically reviewed and not an exhaustive evidence review.** This is childhood TB-prevention evidence, not BCG treatment for bladder cancer or other indications.

Each estimate retains its outcome, population, comparator, follow-up, measure, uncertainty, source IDs and limitations. The source registry records a direct link, publication/revision date where known and the section to check.

- WHO 2025 report: global **2024 incidence**, not prevalence or an unvaccinated baseline.
- Mangtani 2014: infant trial-subgroup rate ratios. Relative rate reduction and confidence bounds use `100 × (1 − RR)`, reversing the interval endpoints. Follow-up varies across trials.
- Martinez 2022: adjusted odds ratio in children under five who were TB contacts; not a risk ratio or trial efficacy.
- BCG Vaccine AJV product information: product-specific frequency **bands**, with an excluded upper bound. Not confidence intervals or excess risks against controls. Observation window and age-specific rates are not provided in that table.
- WHO reaction sheet: local reaction description is a qualitative expectation, not an invented exact percentage. The sheet is historical (2012).

Sources: [WHO incidence](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/tb-disease-burden/1-1-tb-incidence), [Mangtani 2014](https://doi.org/10.1093/cid/cit790), [Martinez 2022](https://stacks.cdc.gov/view/cdc/131794), [AJV product information](https://www.medicines.org.uk/emc/product/9890/smpc), [WHO reactions](https://cdn.who.int/media/docs/default-source/pvg/global-vaccine-safety/bcg-vaccine-rates-information-sheet.pdf), [WHO BCG position paper](https://www.who.int/publications/i/item/who-wer9308-73-96), [WHO TB background](https://www.who.int/news-room/fact-sheets/detail/tuberculosis), [CDC BCG background](https://www.cdc.gov/tb/vaccines/index.html).

## Gaps are deliberate

Null means not established, never zero. No matched baseline, absolute number of cases prevented, severity weight, personal score or net benefit is calculated. Age, sex and geographic groups do not personalise the evidence; global figures are not silently mapped onto the site's geographic groupings. Newborn trial evidence is not automatically applicable to an adult selection. No arbitrary rare/common threshold or severity position is assigned.

Full study disclosures, funding, individual exclusions, systematic search completeness, outcome-specific certainty grading and independent clinical review remain pending. Manufacturer documentation is identified as such. These are distinct types of evidence and must not be pooled into one probability.

## Update workflow

Edit the canonical JSON and add sources before using new values. Run:

```sh
python3 scripts/embed-bcg.py
python3 scripts/validate-bcg.py
```

The validator checks provenance completeness and numerical consistency, not whether clinical evidence is correct. Browser-review changes to BCG and non-BCG states. Publish `dist/` to Sites. For GitHub Pages, copy `dist/index.html` to repository-root `index.html` and `dist/data/bcg.json` to `data/bcg.json`; keep the snapshot in sync.

The world map is the original linked WHO 2025 report Figure 1.1.4 (2024 country incidence), loaded from WHO’s image server; it needs an internet connection. It is not relabelled as prevalence or custom regional averages. The original numerical legend categories and source attribution remain visible. Its palette is adapted in the frontend: green for lower incidence, red for higher incidence, with neutral text, boundaries and missing-data grey retained. Both countries and legend swatches receive the same transformation; the source image and data values are unchanged. The adaptation is explicitly attributed and is not endorsed by WHO. The tools detect both a development `dist/` layout and a repository-root GitHub Pages layout.
