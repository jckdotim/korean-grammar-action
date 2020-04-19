# 한국어 맞춤법 검사기

# 소개

한국어 맞춤법 검사를 해줍니다. PR에서 추가된 한국어 문장을 읽어 맞춤법이 틀렸다면 올바른 방향으로 제안해 줍니다.

# 추가 방법

`.github/workflows`에 다음 항목을 추가합니다.

```
name: CI

on: [pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: "맞춤법 검사"
      uses: jckdotim/korean-grammar-action@v0.2.5
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
