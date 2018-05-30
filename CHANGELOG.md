# Change Log

## [0.13.1](https://github.com/bunq/sdk_python/tree/0.13.1) 

[Full Changelog](https://github.com/bunq/sdk_python/compare/0.13.0...0.13.1)

**Closed issues:**

- Move to new sandbox env.  [\#98](https://github.com/bunq/sdk_python/issues/98)

**Merged pull requests:**

- Move to new sandbox bunq/sdk_python#98 [\#99](https://github.com/bunq/sdk_python/pull/99) ([OGKevin](https://github.com/OGKevin))

## [0.13.0](https://github.com/bunq/sdk_python/tree/0.13.0) (2018-03-20)

[Full Changelog](https://github.com/bunq/sdk_python/compare/0.12.4...0.13.0)

**Implemented enhancements:**

- Add zappr integration for better quality control  [\#62](https://github.com/bunq/sdk_python/issues/62)
- Add more information to template [\#60](https://github.com/bunq/sdk_python/issues/60)
- Add response id to error messages from failed requests  [\#59](https://github.com/bunq/sdk_python/issues/59)

**Fixed bugs:**

- Token request ideal is missing id attribute in response. [\#67](https://github.com/bunq/sdk_python/issues/67)
- Field ID is missing from MasterCardAction [\#54](https://github.com/bunq/sdk_python/issues/54)
- TokenQrRequestIdeal returns the wrong type [\#53](https://github.com/bunq/sdk_python/issues/53)

**Closed issues:**

- bunq update 7  [\#75](https://github.com/bunq/sdk_python/issues/75)

**Merged pull requests:**

- Bunq update 7  [\#76](https://github.com/bunq/sdk_python/pull/76) ([OGKevin](https://github.com/OGKevin))
- Regenerate code for release [\#74](https://github.com/bunq/sdk_python/pull/74) ([OGKevin](https://github.com/OGKevin))
- Regenerated code to add object types. \(bunq/sdk\_python\#53\) [\#70](https://github.com/bunq/sdk_python/pull/70) ([OGKevin](https://github.com/OGKevin))
- Bunq/sdk python\#67 add missing token qr id field [\#69](https://github.com/bunq/sdk_python/pull/69) ([OGKevin](https://github.com/OGKevin))
- Added missing id field to mastercard action. \(bunq/sdk\_python\#54\) [\#66](https://github.com/bunq/sdk_python/pull/66) ([OGKevin](https://github.com/OGKevin))
- Feature/bunq/sdk python\#59 add response id to request error [\#64](https://github.com/bunq/sdk_python/pull/64) ([OGKevin](https://github.com/OGKevin))
- Configure Zappr [\#63](https://github.com/bunq/sdk_python/pull/63) ([OGKevin](https://github.com/OGKevin))
- \(bunq/sdk\_python\#60\) improve issue and pr template [\#61](https://github.com/bunq/sdk_python/pull/61) ([OGKevin](https://github.com/OGKevin))

## [0.12.4](https://github.com/bunq/sdk_python/tree/0.12.4) (2017-12-21)
[Full Changelog](https://github.com/bunq/sdk_python/compare/0.12.3...0.12.4)

**Implemented enhancements:**

- Make sure received signatures headers are correctly cased [\#51](https://github.com/bunq/sdk_python/issues/51)
- Introduce from\_json method  [\#50](https://github.com/bunq/sdk_python/issues/50)
- Return base class from createFromJsonString [\#49](https://github.com/bunq/sdk_python/issues/49)
- CHANGELOG.md is empty [\#46](https://github.com/bunq/sdk_python/issues/46)
- Improve decoder to recognise child object  [\#42](https://github.com/bunq/sdk_python/issues/42)
- Generated CHANGELOG.md :clap:. \(bunq/sdk\_python\#46\) [\#47](https://github.com/bunq/sdk_python/pull/47) ([OGKevin](https://github.com/OGKevin))

**Closed issues:**

- Python doesn't want CamelCase  [\#45](https://github.com/bunq/sdk_python/issues/45)

**Merged pull requests:**

- Feature/make sure headers are correctly cased bunq/sdk python\#51 [\#57](https://github.com/bunq/sdk_python/pull/57) ([OGKevin](https://github.com/OGKevin))
- Feature/improve decoder bunq/sdk python\#42 [\#56](https://github.com/bunq/sdk_python/pull/56) ([OGKevin](https://github.com/OGKevin))
- Renamed camelCase methods. \(bunq/sdk\_python\#45\) [\#48](https://github.com/bunq/sdk_python/pull/48) ([OGKevin](https://github.com/OGKevin))

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
