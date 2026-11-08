# Put this project on GitHub

## 1. Review what will be published

Open the `inbox-reply-helper` folder and check that it contains only the project files you intend to share. The included dataset is fictional. Never add real inbox exports, `.env` files, OAuth client secrets, access tokens, or personal email content.

## 2. Create an empty GitHub repository

1. Sign in at [github.com](https://github.com).
2. Select **New repository**.
3. Name it `inbox-reply-helper` and add a short description, such as “A review-first email follow-up triage prototype.”
4. Choose **Public** if you want employers to view it. Choose **Private** if you want to review it before sharing.
5. Leave **Add a README**, **.gitignore**, and **license** unchecked because those files are already in this folder (you can add a license later).
6. Create the repository and copy its HTTPS URL, which looks like `https://github.com/YOUR-USERNAME/inbox-reply-helper.git`.

## 3. Push this folder

Open PowerShell or a terminal in the `inbox-reply-helper` folder and run:

```bash
git init
git add README.md GITHUB_SETUP.md app.py sample_threads.json .gitignore
git commit -m "Add inbox reply helper prototype"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/inbox-reply-helper.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If Git asks you to authenticate, finish sign-in through GitHub's supported browser flow; do not paste a password or token into this project.

## 4. Copy the project link for Handshake

After the push succeeds, open the repository page on GitHub and copy the browser URL, for example `https://github.com/YOUR-USERNAME/inbox-reply-helper`. Add that URL in the **Projects** section of your Handshake profile with a concise description of what you built and what you learned.

If you later add a live demo, include both the demo URL and the repository URL in the project description.
