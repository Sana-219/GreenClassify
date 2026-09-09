# GreenClassify - Vercel and Render Deployment Guide

The web UI runs on Vercel. TensorFlow and the model run on Render as a separate
Flask service. The Vercel app calls Render through `MODEL_API_URL`.

## Prerequisites
- A Vercel account (free at https://vercel.com)
- Git installed on your machine
- The real model artifact, not only its Git LFS pointer

## Deployment Steps

### 1. Prepare Your Project
Ensure all required files are in place:
- `vercel.json` - Vercel configuration
- `wsgi.py` - WSGI entry point
- `api/index.py` - Serverless function entry point
- `requirements-prod.txt` - Production dependencies (optional, uses requirements.txt by default)
- `.vercelignore` - Files to exclude from deployment

### 2. Initialize Git Repository (if not already done)
```bash
cd /Users/pranav/Downloads/GreenClassify-main
git init
git add .
git commit -m "Initial commit for Vercel deployment"
```

### 3. Push to GitHub
```bash
# Create a new repository on GitHub
git remote add origin https://github.com/YOUR_USERNAME/GreenClassify.git
git branch -M main
git push -u origin main
```

### 4. Deploy the model service to Render

1. Ensure Git LFS is installed and the model is present before pushing:
  ```bash
  git lfs install
  git lfs pull
  ```
2. In Render, select **New > Blueprint**, choose the repository, and apply the
  included `render.yaml`.
3. Copy the resulting public service URL, such as
  `https://greenclassify-model.onrender.com`.

The Render service exposes `GET /health` and `POST /predict`.

### 5. Deploy the UI to Vercel

#### Option A: Using Vercel CLI
```bash
# Install Vercel CLI globally
npm install -g vercel

# Deploy from project directory
cd /Users/pranav/Downloads/GreenClassify-main
vercel
```

#### Option B: Using Vercel Dashboard
1. Go to https://vercel.com/dashboard
2. Click "New Project"
3. Select "Import Git Repository"
4. Choose your GitHub repository
5. Vercel will auto-detect the Flask framework
6. Click "Deploy"

### 6. Configure the Vercel Environment Variable
In Vercel Dashboard:
1. Go to Settings > Environment Variables.
2. Add `MODEL_API_URL` with the Render service URL.
3. Redeploy.

## Important Notes

⚠️ **Model File Size**: Ensure your model file is under Vercel's size limits:
- Free tier: 5MB max per serverless function
- Pro/Enterprise: Larger limits available

If your model exceeds limits, consider:
- Using a cloud storage service (AWS S3, Google Cloud Storage)
- Compressing the model
- Using model quantization

⚠️ **Memory Limits**:
- Free tier: 512MB
- Pro tier: 3008MB (configured in vercel.json)

⚠️ **Timeout Limits**:
- Free tier: 10 seconds
- Pro tier: Up to 60 seconds (configured in vercel.json)

The current `vercel.json` is configured for Pro tier. For free tier, adjust:
```json
{
  "functions": {
    "flask/app.py": {
      "memory": 512,
      "maxDuration": 10
    }
  }
}
```

## Troubleshooting

### 1. Model Not Found
Ensure `vegetable_classification.h5` is in the repository and not in `.vercelignore`

### 2. Dependencies Installation Fails
- Check Python version compatibility
- Use `requirements-prod.txt` with optimized dependencies
- Consider removing unnecessary dependencies

### 3. Timeout Errors
- Optimize model loading (use lazy loading)
- Consider using model caching
- Upgrade to Vercel Pro

### 4. Memory Issues
- Reduce model size
- Use model quantization
- Clear temporary files after processing

## Deployment Variants

### Variant 1: With Netlify (alternative to Vercel)
```bash
npm install -g netlify-cli
netlify deploy --prod
```

### Variant 2: With Railway
```bash
npm install -g @railway/cli
railway up
```

## Post-Deployment

1. **Test your deployment**:
   ```bash
   curl https://your-vercel-app.vercel.app/
   ```

2. **Monitor logs**:
   - Vercel Dashboard → Deployments → View Logs

3. **Set up custom domain** (optional):
   - Vercel Dashboard → Settings → Domains

## API Endpoints

After deployment, your app will be available at:
- `https://your-vercel-app.vercel.app/` - Home page
- `https://your-vercel-app.vercel.app/prediction.html` - Prediction page
- `https://your-vercel-app.vercel.app/result` - API endpoint (POST image for classification)

## Database/Storage

If you need persistent storage:
- Use Vercel KV (Redis)
- Integrate PostgreSQL or MongoDB
- Use external cloud storage (S3, etc.)

## Rollback

To rollback to a previous deployment:
1. Vercel Dashboard → Deployments
2. Select the previous deployment
3. Click "Promote to Production"

## Additional Resources

- [Vercel Python Deployment Docs](https://vercel.com/docs/concepts/functions/serverless-functions/python)
- [Flask on Vercel](https://vercel.com/docs/frameworks/flask)
- [Vercel Pricing](https://vercel.com/pricing)
