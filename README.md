# Florence's 5th Birthday Party Invitation 🦄

A magical interactive invitation website for Florence's 5th birthday party!

## 🎉 Party Details
- **Date:** Saturday, October 18th, 2025
- **Time:** 11:30 AM - 1:00 PM
- **Location:** SuperZu Princess Room, Dingley Village
- **RSVP:** Limited to 13 special friends!

## 🚀 Quick Setup with GitHub Pages

### Option 1: Direct GitHub Upload (Easiest)
1. Go to [github.com/new](https://github.com/new)
2. Name your repository: `florence-turns-5`
3. Make it public
4. Click "Create repository"
5. Click "uploading an existing file"
6. Drag all files from this folder
7. Commit changes
8. Go to Settings → Pages
9. Source: Deploy from branch (main)
10. Your site will be live at: `https://[your-username].github.io/florence-turns-5`

### Option 2: Using Git Commands
```bash
# Initialize and push to GitHub
cd "/Users/petermoulton/Documents/Florence 5th Birthday"
git init
git add .
git commit -m "Florence's 5th birthday party invitation"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/florence-turns-5.git
git push -u origin main
```

Then enable GitHub Pages in repository settings.

## 📱 Features
- ✨ Interactive unicorn animations
- ⏰ Live countdown timer
- 📍 One-click directions
- 📅 Add to calendar
- 🎈 RSVP form with spot counter
- 📧 Email notifications (when connected to backend)

## 🔧 Customization

### To change party details:
Edit the HTML file and update:
- Date/time in the event details section
- Location information
- RSVP limit (currently set to 13)
- Contact phone number

### To add backend RSVP handling:
The form currently saves to localStorage for demo. To connect to a real backend:

1. **Option A: Google Forms** (Free & Easy)
   - Create a Google Form with matching fields
   - Use the form's embed code
   - Replace the current form section

2. **Option B: Netlify Forms** (Free tier available)
   - Deploy to Netlify instead
   - Add `netlify` attribute to form
   - Netlify handles form submissions

3. **Option C: Custom Backend**
   - Set up endpoint (e.g., using Netlify Functions)
   - Update the form submission handler
   - Store in database of choice

## 📊 Tracking RSVPs

Current demo saves to browser localStorage. To view RSVPs in console:
```javascript
JSON.parse(localStorage.getItem('florenceRSVPs'))
```

## 🎨 Color Scheme
- Pink: #FF6B9D
- Purple: #C66FD2
- Blue: #7C9BF2
- Mint: #84fab0

## 📝 License
Made with 💖 for Florence's special day!