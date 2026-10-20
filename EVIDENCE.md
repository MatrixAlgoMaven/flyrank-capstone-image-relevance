# Evidence and Verification

## Current Status

Project setup and initial documentation are complete. The backend implementation and evaluation evidence are pending.

## Required Evidence Checklist

- [ ] Image batch processing produces schema-valid metadata.
- [ ] Low-confidence image classifications are flagged.
- [ ] Relevant images rank above unrelated candidates.
- [ ] A fox post rejects an incompatible wolf image with an explained category mismatch.
- [ ] No suitable image produces a "no confident match" response with reasons.
- [ ] Background jobs expose progress and retry failed operations.
- [ ] AI-call logs record vision and embedding operations, status, and cost.
- [ ] API validation errors return appropriate 4xx responses.
- [ ] Automated tests pass.
- [ ] Evaluation script reports top-1 precision on at least 10 labelled posts.
- [ ] The measured evaluation result matches the value reported in `README.md`.

## Evidence to Add

As implementation progresses, add reproducible test commands, actual outputs, screenshots where useful, and measured evaluation results. Do not mark an item complete until it has been verified.
