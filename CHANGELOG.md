# CHANGELOG


## v0.8.1 (2025-03-06)

### Bug Fixes

- Revert handling 18 byte data
  ([#48](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/48),
  [`ace5ae2`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/ace5ae25c2f4dc362d7f625e4e4afe2e20b3272d))

This reverts the check that was changed in #33 because it caused a regression in
  https://github.com/home-assistant/core/issues/139917

### Chores

- **ci**: Bump python-semantic-release/python-semantic-release from 9.20.0 to 9.21.0 in the
  github-actions group ([#44](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/44),
  [`298a426`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/298a426366eabea9361f5f0ffb85b71a49fc9d66))

chore(ci): bump python-semantic-release/python-semantic-release

Bumps the github-actions group with 1 update:
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).

Updates `python-semantic-release/python-semantic-release` from 9.20.0 to 9.21.0 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.rst)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.20.0...v9.21.0)

--- updated-dependencies: - dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production

update-type: version-update:semver-minor

dependency-group: github-actions ...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump myst-parser from 1.0.0 to 3.0.1
  ([#45](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/45),
  [`106260a`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/106260a44b0f47c908e2bde302af31202ee9795a))

Bumps [myst-parser](https://github.com/executablebooks/MyST-Parser) from 1.0.0 to 3.0.1. - [Release
  notes](https://github.com/executablebooks/MyST-Parser/releases) -
  [Changelog](https://github.com/executablebooks/MyST-Parser/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/executablebooks/MyST-Parser/compare/v1.0.0...v3.0.1)

--- updated-dependencies: - dependency-name: myst-parser dependency-type: direct:production

update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump sphinx from 5.3.0 to 6.2.1
  ([#43](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/43),
  [`baaecb6`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/baaecb68314ed7a0c2f7e30f8800856e4d7ff3a6))

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump sphinx-rtd-theme from 2.0.0 to 3.0.2
  ([#47](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/47),
  [`5513390`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/5513390e1bec897ae81924e65df9ce5fd563f54e))

- **deps-dev**: Bump pytest from 7.4.3 to 8.3.4
  ([#42](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/42),
  [`a7df929`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/a7df9294d49860f8e9e2d0c2bc3cf32a21585838))

- **deps-dev**: Bump pytest from 8.3.4 to 8.3.5
  ([#46](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/46),
  [`7d48f63`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/7d48f6375cdd7b75a7af4ef26a05c277b0632e5c))

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.3.4 to 8.3.5. - [Release
  notes](https://github.com/pytest-dev/pytest/releases) -
  [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest/compare/8.3.4...8.3.5)

--- updated-dependencies: - dependency-name: pytest dependency-type: direct:development

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **pre-commit.ci**: Pre-commit autoupdate
  ([#41](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/41),
  [`f90b502`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/f90b502079c9cff4266680c1af71836fa0ef522b))

updates: - [github.com/commitizen-tools/commitizen: v4.2.1 →
  v4.4.1](https://github.com/commitizen-tools/commitizen/compare/v4.2.1...v4.4.1) -
  [github.com/PyCQA/isort: 6.0.0 → 6.0.1](https://github.com/PyCQA/isort/compare/6.0.0...6.0.1)

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>


## v0.8.0 (2025-02-23)

### Features

- Add support for model 20 ([#40](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/40),
  [`79c369f`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/79c369f2c39d42fd17e5df7552f2c756b995b8bf))


## v0.7.1 (2025-02-23)

### Bug Fixes

- Handle devices with a 18 byte manufacturer data
  ([#33](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/33),
  [`6267295`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/6267295dedf26d0ea49a8ec264060375f76045f1))

### Chores

- Create dependabot.yml
  ([`186ce58`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/186ce58804a61436285a7fc6d5c42c37a0d34cfd))

- **ci**: Bump the github-actions group with 8 updates
  ([#34](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/34),
  [`2a52558`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/2a5255896d414418c0ee2d916f52ac06beb4e5d2))

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

Co-authored-by: J. Nick Koston <nick@koston.org>

- **deps**: Bump bluetooth-sensor-state-data from 1.6.2 to 1.7.5
  ([#39](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/39),
  [`9b09519`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/9b0951910fd4feb4f904056d052d3edeaf23d132))

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump myst-parser from 0.18.1 to 1.0.0
  ([#36](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/36),
  [`f263fb8`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/f263fb8e540eb9518e31ae698233b06b838b7bb7))

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump sensor-state-data from 2.18.0 to 2.18.1
  ([#35](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/35),
  [`187f266`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/187f2664e8726f28993bde349e8fb6b18fcd7595))

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump sphinx-rtd-theme from 1.3.0 to 2.0.0
  ([#37](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/37),
  [`85f8236`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/85f8236c85cf516dc6bbc5195cb509c78ff519ce))

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps-dev**: Bump pytest-cov from 3.0.0 to 6.0.0
  ([#38](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/38),
  [`cd71827`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/cd71827119c1bc86e222ecd03f838570489299a3))

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **pre-commit.ci**: Pre-commit autoupdate
  ([#22](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/22),
  [`11d2d88`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/11d2d88bf6049664cac7f18e443e9145e9483028))

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

- **pre-commit.ci**: Pre-commit autoupdate
  ([#23](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/23),
  [`040997b`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/040997b7fa0971cafca12c3d40e40baabc210aeb))

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

- **pre-commit.ci**: Pre-commit autoupdate
  ([#24](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/24),
  [`16b4fe5`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/16b4fe5b74f4879a95db2df5327e07f699baca8d))

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

- **pre-commit.ci**: Pre-commit autoupdate
  ([#25](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/25),
  [`4e737b3`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/4e737b3357e14bd93f3fb02187b9a1e345e4f386))

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

- **pre-commit.ci**: Pre-commit autoupdate
  ([#26](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/26),
  [`9493003`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/9493003ef3e2e50f051017d7cab1a8645910d6f8))

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

- **pre-commit.ci**: Pre-commit autoupdate
  ([#27](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/27),
  [`239c673`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/239c673b2f4c999ed4160a65847bddfdb7aac9f3))

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

- **pre-commit.ci**: Pre-commit autoupdate
  ([#29](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/29),
  [`f4f3a99`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/f4f3a99d3037a890695b22f12a13026ab1b0b134))

- **pre-commit.ci**: Pre-commit autoupdate
  ([#30](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/30),
  [`8220256`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/8220256a59d214557720de674938d597a62c15b7))

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

- **pre-commit.ci**: Pre-commit autoupdate
  ([#31](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/31),
  [`ede3aa3`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/ede3aa30f98e200d9401be006e4e6d7b7fde87b8))

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

- **pre-commit.ci**: Pre-commit autoupdate
  ([#32](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/32),
  [`841a2ae`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/841a2aeb42e181c45eb693264b7095f98d1eb8ae))

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>


## v0.7.0 (2024-07-03)

### Chores

- **pre-commit.ci**: Pre-commit autoupdate
  ([#20](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/20),
  [`1f37fa1`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/1f37fa1db3e6e42def14e1303e25595de1006f73))

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

### Features

- Add mappings for ws23 ([#21](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/21),
  [`3dca812`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/3dca812a7d09e37cff63ac73630f0bf38779ce5e))


## v0.6.2 (2023-12-29)

### Bug Fixes

- Release process ([#18](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/18),
  [`3cb2118`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/3cb21182898235346178b9ff8b3a941aaffd69e0))


## v0.6.1 (2023-12-29)

### Bug Fixes

- Battery percentage wobble ([#12](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/12),
  [`484139a`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/484139a9135a0bf69e7d3a9eb4d18ad77631ed7e))

### Chores

- Fix ci ([#13](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/13),
  [`be355e0`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/be355e002675a91978105f35b2dface739f7b195))

- Fix release process ([#14](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/14),
  [`3cdc437`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/3cdc437d3ceb89a3d1978b01e8a655d742114a38))

- Fix release process ([#15](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/15),
  [`627b678`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/627b67820caf55d83f85977a36df29aa45441277))

- More ci fixes ([#16](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/16),
  [`d09abee`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/d09abeec4beb40f4a4e750a329a9d426d1d9380e))

- More ci fixes ([#17](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/17),
  [`d0f8c05`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/d0f8c0583155ae3fa57c4b8ab338512bd38194f1))


## v0.6.0 (2022-12-29)

### Features

- Add mapping for id 27 ([#10](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/10),
  [`9e64a79`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/9e64a79f733c05ca469791943b0411a1fcec45be))


## v0.5.0 (2022-12-29)

### Features

- Add python 3.11 support ([#9](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/9),
  [`1c997d1`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/1c997d101961aaaadedd6be2a298d0fd3385944e))


## v0.4.0 (2022-11-13)

### Features

- Add support for device 0x18 ([#8](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/8),
  [`7599842`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/7599842522f845a2a39e3ec69bc9d1d7901c9044))


## v0.3.2 (2022-09-18)

### Bug Fixes

- Ignore garbage data ([#6](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/6),
  [`808da03`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/808da0307bf9ec8a10bbe35a3c605f7c3dac0c3a))


## v0.3.1 (2022-08-25)

### Bug Fixes

- Data alignment ([#5](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/5),
  [`12cac30`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/12cac307f7dd58bd2964b2e28d0747e5397ff1ee))


## v0.3.0 (2022-08-25)

### Features

- Implement rounding ([#4](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/4),
  [`7a534ee`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/7a534ee0f5fd930113c5f95e30807dafe87e5e48))


## v0.2.0 (2022-08-25)

### Features

- Init parser ([#3](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/3),
  [`a4b521a`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/a4b521ab737408b1633812a4e0b6015f0ee7ce00))


## v0.1.0 (2022-08-25)

### Bug Fixes

- Use bluetooth-data-tools for short_address
  ([#2](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/2),
  [`536efc4`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/536efc4d114262b5794a4868024817fd194e785c))

### Chores

- Initial commit
  ([`df09661`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/df09661efddd9fcacd99e4aa446a6656b468c3a0))

### Features

- Init repo ([#1](https://github.com/Bluetooth-Devices/thermobeacon-ble/pull/1),
  [`195526e`](https://github.com/Bluetooth-Devices/thermobeacon-ble/commit/195526ed5fe312f65194b2f0d48239127da0e808))
