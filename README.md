# Create Your Utopia

Landing page plus a live Blueprint generator.

- `index.html`: the page.
- `api/blueprint.js`: a Vercel function. It takes the visitor's idea, asks Claude for a Blueprint, and returns it. Your API key stays on the server and is never sent to visitors.
- `package.json`: tells Vercel to install the Anthropic SDK.

## Deploy

### 1. Get an Anthropic API key and set a spend limit
1. Sign in at console.anthropic.com and add billing.
2. Go to **API Keys** and create a key. Copy it somewhere safe; you'll paste it into Vercel in step 3.
3. Go to **Limits** and set a monthly spend limit (for example $20). Each Blueprint costs a few cents, and this caps what a busy day or a misuser can cost you.

### 2. Put the files on GitHub
1. Sign in at github.com and click **New repository**. Name it `create-your-utopia`. Public or private both work.
2. On the new repo page, click **uploading an existing file**.
3. Drag in `index.html`, `package.json`, `README.md` and the whole `api` folder.
4. Click **Commit changes**.

### 3. Deploy on Vercel
1. Sign up at vercel.com with **Continue with GitHub**.
2. Click **Add New → Project**, then **Import** next to `create-your-utopia`.
3. Leave Framework Preset as **Other**. Open **Environment Variables** and add:
   - Name: `ANTHROPIC_API_KEY`
   - Value: your key from step 1
4. Click **Deploy**. After a minute you get a public link like `create-your-utopia.vercel.app`.

### 4. Test it
Open the link, type an idea, and click **Draw my Blueprint**. If it says the tool "isn't set up yet", the API key is missing or wrong: fix it under Project → Settings → Environment Variables, then redeploy.

## Change things later

- **Booking link:** in `index.html`, find `const BOOKING_URL = "";` and put your Calendly or Cal.com link between the quotes. Commit on GitHub and Vercel redeploys on its own.
- **Model:** the function uses Claude Opus 5.5. To use a cheaper model, add a Vercel environment variable `BLUEPRINT_MODEL` set to `claude-haiku-5-5` (fastest and cheapest) or `claude-sonnet-5-5`, then redeploy.
- **Usage limit:** each visitor can draw 5 Blueprints per hour. Change `MAX_PER_WINDOW` in `api/blueprint.js`. This limit is best-effort; the spend limit from step 1 is your real safety net.
