# RSVP Setup Instructions

## Current Status
⚠️ **IMPORTANT**: RSVPs are currently only stored locally in the browser and Adelaide will NOT receive them!

## Option 1: Netlify Forms (Recommended - FREE)

1. Deploy site to Netlify (free account)
2. Add `netlify` attribute to form
3. Netlify automatically handles form submissions
4. Set up email notifications to Adelaide

### Implementation:
Replace the current form tag in index.html with:
```html
<form class="rsvp-form" netlify netlify-honeypot="bot-field" action="/thank-you">
    <input type="hidden" name="form-name" value="florence-rsvp">
```

### Setup Email Notifications:
1. Go to Netlify Dashboard → Forms
2. Click "Settings & Usage"
3. Add email notification to: adelaide@example.com
4. Submissions will be emailed automatically

## Option 2: Google Forms (Simple)

1. Create a Google Form with fields:
   - Parent Name
   - Child Name
   - Number of Children
   - Dietary Requirements
   - Contact Email

2. Get the embed code
3. Replace current form with Google Form iframe
4. Set up email notifications in Google Forms

## Option 3: Formspree (Free tier - 50 submissions/month)

Replace form action with:
```html
<form class="rsvp-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

1. Sign up at formspree.io
2. Create a form
3. Add adelaide's email
4. Copy form ID
5. Replace YOUR_FORM_ID above

## Option 4: SMS Notifications (using Twilio)

For SMS notifications, you'll need:
1. Twilio account ($)
2. Backend service (Netlify Functions or similar)
3. Code to send SMS to Adelaide's phone

## Privacy & Security Notes

- Never store RSVP data in public GitHub repos
- Use environment variables for API keys
- Ensure form has privacy notice
- Consider CAPTCHA to prevent spam

## Current Privacy Implementation

The current form data:
- ✅ Is NOT publicly accessible
- ✅ Stays only in user's browser
- ❌ Does NOT get sent to Adelaide
- ❌ Has no backend storage

## Quick Fix for GitHub Pages

Since you're using GitHub Pages, the easiest solution is:

1. **Use Formspree** (free, no backend needed)
2. **Or deploy to Netlify instead** (also free, better for forms)

## To Implement Now:

Choose one option above and I can update the code immediately. Which would you prefer?