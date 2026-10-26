# Port release updater

The `.github/workflows/port-release-updates.yml` workflow checks the ports listed in `.github/port-updates.json` once a week and on demand. Each port runs in its own macOS job.

For a newer livecheck version, the workflow uses seaport to update the Portfile version, revision and distfile checksums. It then runs `port lint --nitpick` and a full source install with `sudo port -vst install`. A failed update, lint or install does not produce a PR.

## Review-first behavior

- A push to the setup review branch opens a **draft preview PR in this fork** only after the build passes.
- Manual workflow runs can target this fork (`preview`), submit to MacPorts upstream (`upstream`), or only test (`build-only`).
- Scheduled runs build and report updates only by default. To let scheduled runs open upstream PRs after the example is reviewed, set the repository Actions variable `ENABLE_MACPORTS_UPSTREAM_PRS` to `true`.
- Upstream PR publication uses the `MACPORTS_PR_TOKEN` Actions secret. It is only passed to the final PR creation step, after source code has finished building.
- Fork draft PR creation uses the workflow token. In repository Settings → Actions → General, allow GitHub Actions to create pull requests.

The upstream token needs permission to push a branch to this fork and create a pull request against the public `macports/macports-ports` repository. Do not add it to build steps.

## Add another port

1. Add an entry to `.github/port-updates.json` with the MacPorts port name and path.
2. Ensure its Portfile has a working `livecheck` and source distfile checksum stanza. Seaport uses the livecheck result to calculate the new checksum fields.
3. Run the workflow manually with the new port selected and destination `build-only` before enabling PR publication.

The first version supports standard livecheck-based version bumps. Ports requiring dependency lockfile regeneration or custom Portfile changes should be added only after their update procedure is configured and tested separately.
