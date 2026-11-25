# Statistics review template

Structure for reviewing a student's R or SPSS analysis (course template 04). Use the student's own numbers throughout.

## What to ask for

- Study topic (1 to 2 lines), design, sampling and N
- Variables: name = type/scale, role (for example `ease = Likert 1 to 5, DV`)
- Known data issues: missing data, outliers, non-normality, unequal variances
- Correction for multiple comparisons, if any
- Research questions, code or syntax, and the pasted output (descriptives, assumption tests, model output)

## What to return, in this order

1. **Quick verdict**
   - Test choice: appropriate or questionable, and why
   - Major assumption risks
   - Biggest fix to try first

2. **Assumption check table**

   | Assumption | Evidence from the output | Pass / Borderline / Fail | Why it matters | What to do |
   |---|---|---|---|---|

3. **Test-by-test review**, for each test or model:
   - Purpose, and whether it is the right test
   - Key statistics copied from the output: statistic, df, p, CI, effect size
   - Interpretation in plain English (2 to 3 sentences)
   - Advanced note (3 bullets at most)
   - If the test is wrong: the right one, with code

4. **Multiple comparisons and model fit**: where error inflation is a risk, how to control it (Bonferroni, FDR), and what the fit measures mean in practice.

5. **Example report sentences**: two or three APA-style sentences per main result, filled with the student's numbers.

6. **Next steps and sensitivity checks**: what to rerun (robust or nonparametric alternatives, transformations, mixed models), and a plain statement on statistical power.

7. **Limitations**: 3 to 5 bullets specific to this data and analysis.

8. **Code templates**: R and SPSS syntax for each recommended correction.

## Common pitfalls to look for

- Treating single Likert items as interval data without comment
- Many t-tests where one model would do
- Within-subject data analyzed as between-subject
- Ignoring missing data or dropping it silently
- Cronbach's alpha reported for a scale that is multidimensional
- Reporting p-values without effect sizes
