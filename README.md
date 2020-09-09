# Check labels in PR

## Setup

Create a `.yml` file under the `.github/workflows/` directory in your repository with the following contents:

```
name: Expect labels
on:
  pull_request:
   types: [opened, labeled, unlabeled, synchronize]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: erdostw/tw-check-label@0.0.1
      with:
        github-token: '${{ secrets.GITHUB_TOKEN }}'
```
