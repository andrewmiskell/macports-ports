# Example automated port update PR

The updater uses the title and checklist format seen in MacPorts port update PRs. This is a format preview; the tested-on and verification details are filled from the successful GitHub Actions run.

**Example title**

`aws-sso-cli: update to 2.3.4`

**Example body**

#### Description

Update aws-sso-cli to 2.3.4.

###### Type(s)

- [ ] bugfix
- [x] enhancement
- [ ] security fix

###### Tested on

macOS 15.7.9 (arm64), GitHub Actions

###### Verification

Have you

- [x] followed the [Commit Message Guidelines](https://trac.macports.org/wiki/CommitMessages)?
- [x] squashed and [minimized your commits](https://guide.macports.org/#project.github)?
- [ ] checked for other open [pull requests](https://github.com/macports/macports-ports/pulls) for the same change?
- [ ] referenced an existing Trac ticket, if applicable?
- [x] checked the Portfile with `port lint --nitpick`?
- [ ] tried existing tests with `sudo port test`?
- [x] tried a full install with `port -v install`?
- [ ] tested basic functionality of all binary files?

The PR is opened only after the updated port passes lint and a full source install on a macOS runner. The automation opens a draft preview PR in this fork after the build passes; upstream publication stays disabled until explicitly enabled.
