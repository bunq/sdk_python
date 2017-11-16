# Change Log

## [0.12.3](https://github.com/bunq/sdk_python/tree/0.12.3) (2017-11-15)
[Full Changelog](https://github.com/bunq/sdk_python/compare/0.12.2...0.12.3)

**Implemented enhancements:**

- Callback models for holding callback data [\#40](https://github.com/bunq/sdk_python/issues/40)
- Feature/callback models bunq/sdk python\#40 [\#43](https://github.com/bunq/sdk_python/pull/43) ([OGKevin](https://github.com/OGKevin))

**Fixed bugs:**

- ScheduledPayment causes decode error due to Typo [\#44](https://github.com/bunq/sdk_python/issues/44)

## [0.12.2](https://github.com/bunq/sdk_python/tree/0.12.2) (2017-11-08)
[Full Changelog](https://github.com/bunq/sdk_python/compare/0.12.0...0.12.2)

**Implemented enhancements:**

- Add missing fields for cvc endpoint [\#37](https://github.com/bunq/sdk_python/issues/37)
- Missing CARD GENERATED CVC2 endpoint  [\#33](https://github.com/bunq/sdk_python/issues/33)
- More flexibility for sessionContext handling [\#31](https://github.com/bunq/sdk_python/issues/31)
- Added cvc\_endpoint. \#33 [\#34](https://github.com/bunq/sdk_python/pull/34) ([OGKevin](https://github.com/OGKevin))
- Added isSessionExpired\(\) method \#31. [\#32](https://github.com/bunq/sdk_python/pull/32) ([OGKevin](https://github.com/OGKevin))

**Fixed bugs:**

- DraftPayment object field causes converter error  [\#36](https://github.com/bunq/sdk_python/issues/36)

**Merged pull requests:**

- Feature/fix draft payment object \#36 [\#39](https://github.com/bunq/sdk_python/pull/39) ([OGKevin](https://github.com/OGKevin))
- Feature/add missing cvc fields \#37 [\#38](https://github.com/bunq/sdk_python/pull/38) ([OGKevin](https://github.com/OGKevin))

## [0.12.0](https://github.com/bunq/sdk_python/tree/0.12.0) (2017-10-11)
[Full Changelog](https://github.com/bunq/sdk_python/compare/0.11.0...0.12.0)

**Implemented enhancements:**

- Add strictly typed BunqResponses [\#27](https://github.com/bunq/sdk_python/issues/27)
- Better error handling  [\#25](https://github.com/bunq/sdk_python/issues/25)
- Add Pagination [\#20](https://github.com/bunq/sdk_python/issues/20)
- Marked all files in generated dir as generated code. [\#24](https://github.com/bunq/sdk_python/pull/24) ([OGKevin](https://github.com/OGKevin))

**Merged pull requests:**

- cleanup after 27-strictly-typed-response [\#30](https://github.com/bunq/sdk_python/pull/30) ([dnl-blkv](https://github.com/dnl-blkv))
- Add strictly typed responses; fix circular dependencies; improve namespaces [\#28](https://github.com/bunq/sdk_python/pull/28) ([dnl-blkv](https://github.com/dnl-blkv))
- Feature/exception handler [\#26](https://github.com/bunq/sdk_python/pull/26) ([OGKevin](https://github.com/OGKevin))

## [0.11.0](https://github.com/bunq/sdk_python/tree/0.11.0) (2017-09-06)
[Full Changelog](https://github.com/bunq/sdk_python/compare/0.10.0...0.11.0)

**Implemented enhancements:**

- Ignore generated code for reviews  [\#22](https://github.com/bunq/sdk_python/issues/22)
- Feature/git attributes [\#23](https://github.com/bunq/sdk_python/pull/23) ([OGKevin](https://github.com/OGKevin))
- Add pagination [\#21](https://github.com/bunq/sdk_python/pull/21) ([dnl-blkv](https://github.com/dnl-blkv))

## [0.10.0](https://github.com/bunq/sdk_python/tree/0.10.0) (2017-08-22)
[Full Changelog](https://github.com/bunq/sdk_python/compare/0.9.1...0.10.0)

**Implemented enhancements:**

- Add proxy support to Python SDK [\#16](https://github.com/bunq/sdk_python/issues/16)
- Break the SDK's dependence on the bunq.conf file [\#11](https://github.com/bunq/sdk_python/issues/11)
- Response is missing response headers and pagination [\#9](https://github.com/bunq/sdk_python/issues/9)
- cleanup tests \[\#18\] [\#19](https://github.com/bunq/sdk_python/pull/19) ([dnl-blkv](https://github.com/dnl-blkv))
- Changed test class name [\#14](https://github.com/bunq/sdk_python/pull/14) ([OGKevin](https://github.com/OGKevin))
- Load and Save an ApiContext from and to JSON Data [\#13](https://github.com/bunq/sdk_python/pull/13) ([PJUllrich](https://github.com/PJUllrich))
- \#9 Introduce BunqResponse [\#10](https://github.com/bunq/sdk_python/pull/10) ([dnl-blkv](https://github.com/dnl-blkv))

**Closed issues:**

- Tests need a minor cleanup [\#18](https://github.com/bunq/sdk_python/issues/18)

**Merged pull requests:**

- Add proxy support \[\#16\] [\#17](https://github.com/bunq/sdk_python/pull/17) ([dnl-blkv](https://github.com/dnl-blkv))

## [0.9.1](https://github.com/bunq/sdk_python/tree/0.9.1) (2017-08-07)
**Implemented enhancements:**

- Submit this as package to PyPi [\#2](https://github.com/bunq/sdk_python/issues/2)
- Readme for tests [\#5](https://github.com/bunq/sdk_python/pull/5) ([OGKevin](https://github.com/OGKevin))
- Uploaded to PyPi [\#4](https://github.com/bunq/sdk_python/pull/4) ([OGKevin](https://github.com/OGKevin))
- Add first series of unit-tests [\#1](https://github.com/bunq/sdk_python/pull/1) ([OGKevin](https://github.com/OGKevin))

**Fixed bugs:**

- Add Threadsafety for x-bunq-server-signature [\#7](https://github.com/bunq/sdk_python/issues/7)



\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*