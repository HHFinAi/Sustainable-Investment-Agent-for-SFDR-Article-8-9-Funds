# GitHub Desktop Setup Guide

A step-by-step walkthrough for publishing this library to GitHub using GitHub Desktop, including Git identity configuration, repository initialisation, publishing, and day-to-day update workflows.

---

## Part One: Prerequisites

### Install GitHub Desktop

Download GitHub Desktop from [desktop.github.com](https://desktop.github.com/) and install for macOS or Windows. On first launch it will ask you to sign in to a GitHub account; use (or create) the account under which you want this library published.

### Configure Your Identity

GitHub Desktop will ask you to configure your name and email address for Git commits. Use the same email address associated with your GitHub account so that commits are properly attributed. If you are publishing under a professional identity, ensure the name matches how you want to appear in the commit history.

## Part Two: Creating the Repository

### Preparing the Local Folder

Download or extract the library files to a location on your computer. A dedicated folder under your user directory works well, such as `Documents/sustainable-investment-sfdr-prompts` on Windows or `/Users/<yourname>/sustainable-investment-sfdr-prompts` on macOS.

Verify that the folder contains all the required files and subfolders:

```
sustainable-investment-sfdr-prompts/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── .gitignore
├── .gitattributes
├── library/
│   ├── PROMPT_LIBRARY.md
│   └── PROMPT_HEADER.md
└── docs/
    ├── GITHUB_DESKTOP_SETUP.md
    └── CATEGORIES.md
```

### Adding the Local Repository to GitHub Desktop

Open GitHub Desktop. From the **File** menu, select **Add Local Repository**. Browse to the folder containing the library files. Select the folder and click **Add Repository**.

GitHub Desktop will recognise the folder and offer to initialise it as a Git repository if Git has not already been initialised. Click **Create a Repository** to confirm the initialisation.

GitHub Desktop will now display the repository in its main interface, showing the Changes tab with all files marked as new additions. The **Summary** field prompts you for a description of this initial commit. Enter a descriptive message such as:

> Initial release v1.0 — 52-prompt Sustainable Investment library for SFDR Article 8 & 9 funds

and click **Commit to main**. This creates your first commit containing the entire library.

### Publishing to GitHub

With the initial commit in place, the next step is publishing the repository to GitHub so that it exists on the remote server and can be accessed, shared, or cloned.

From the **Repository** menu or the prominent **Publish Repository** button, select **Publish Repository**. A dialog will appear with several configuration options.

The **Name** field defaults to the local folder name but can be customised. Options include:

- `sustainable-investment-sfdr-prompts` (recommended — matches the folder, descriptive, SEO-friendly)
- `sfdr-8-9-prompts`
- `sustainable-investment-prompts`

The **Description** field provides a short summary that appears on the repository's GitHub page. A description such as:

> Institutional-grade prompt library for buy-side Sustainable Investment analysts running SFDR Article 8 & 9 global public equity strategies. 52 prompts across 18 categories.

communicates the purpose effectively.

The **Keep this code private** checkbox determines visibility. For a public resource intended for the broader investment community and to build your professional portfolio, **uncheck this box** to create a public repository.

Click **Publish Repository**. GitHub Desktop will create the repository on GitHub under your account and push the initial commit. When the process completes, a **View on GitHub** link becomes active — click it to view your published library in the browser.

## Part Three: Post-publication Tasks

### Verify Mermaid Rendering

The README contains a Mermaid workflow diagram. Open the repository on GitHub and scroll to the "Workflow Coverage" section. The diagram should render automatically as an SVG. If it does not render (rare, but can happen with very old browsers or corporate proxy caches), the raw mermaid code block is still readable as plain text.

### Verify TOC Anchor Links

Open `library/PROMPT_LIBRARY.md` on GitHub. Click 3–4 of the deeper TOC links (e.g., PROMPT 22 with the controlled-company subheader, PROMPT 47 with the Annex IV/V parenthetical) to confirm they jump correctly. If any link 404s within the page, the fix is a one-character edit to that line's anchor in the TOC.

### Add Topics

On the repository's main GitHub page, click the gear icon next to **About** on the right-hand side and add topics to improve discoverability. Suggested topics:

`sfdr` · `sustainable-investment` · `esg` · `sdr` · `responsible-investment` · `stewardship` · `eu-taxonomy` · `tcfd` · `tnfd` · `pcaf` · `claude` · `prompt-engineering` · `asset-management` · `hedge-fund`

### Add a Short Bio Line

Click **Edit repository details** (pencil icon next to the repository name) and set the repository website to your LinkedIn URL if you would like a direct link back to your professional profile from the repo header.

## Part Four: Day-to-Day Updates

### Making Changes

When you update the library — adding a prompt, revising a prompt, updating the CHANGELOG — GitHub Desktop will automatically detect the changes when you save the file.

In the **Changes** tab you will see the files modified, with a diff view showing exactly what changed. Write a descriptive commit message in the **Summary** field. Good messages follow the form:

- `Add Prompt 53: Financial sector PCAF deep-dive`
- `Update Prompt 22 for UK Corporate Governance Code 2024 revision`
- `Fix typo in Prompt 12 scenario coverage requirement`
- `Bump version to v1.1 in CHANGELOG`

Click **Commit to main**. Then click **Push origin** (top of the window) to upload the commit to GitHub.

### Creating a New Release

After material changes (e.g., ≥5 new prompts, a regulatory overhaul, a version bump), create a GitHub release:

1. Go to the repository page on GitHub.
2. Click **Releases** (right sidebar).
3. Click **Draft a new release**.
4. Create a tag matching the CHANGELOG version (e.g., `v1.1.0`).
5. Write release notes summarising the changes (copy from CHANGELOG).
6. Click **Publish release**.

Releases give the library version anchors that users can cite and pin to.

## Part Five: Troubleshooting

**Commit attribution shows the wrong name.** Go to GitHub Desktop → **Preferences** → **Git** and update the name/email. Only new commits will use the updated values; past commits remain as they were.

**Files showing as modified when nothing changed.** Usually a line-ending issue on Windows. The `.gitattributes` file in this repo forces LF line endings to prevent this; if it still happens, check that your editor isn't silently converting to CRLF.

**Can't push — "non-fast-forward" error.** Someone (maybe another machine, maybe collaborators) has pushed to `main` since your last pull. Click **Pull origin** first, resolve any merge conflicts in GitHub Desktop, then push.

**Want to undo a commit before pushing.** Right-click the commit in the History tab and select **Undo**. This reverts the commit but keeps the changes in your working directory.

**Want to delete the GitHub repo entirely and start again.** On GitHub, go to the repo → **Settings** → scroll to bottom → **Delete this repository**. Type the repo name to confirm. Then in GitHub Desktop, remove the local repo and start over.

---

*For problems not covered above, [GitHub Desktop's official documentation](https://docs.github.com/en/desktop) is the authoritative source.*
