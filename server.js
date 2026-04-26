const express = require('express');
const fetch = require('node-fetch');
const app = express();

const PORT = 3000;

// GANTI USERNAME ANDA
const GITHUB_USER = "bswcorp";

app.get('/api/repos', async (req, res) => {
    try {
        const response = await fetch(`https://api.github.com/users/${GITHUB_USER}/repos`);
        const data = await response.json();

        const result = data.map(repo => ({
            name: repo.name,
            updated: repo.updated_at,
            stars: repo.stargazers_count
        }));

        res.json(result);
    } catch (err) {
        res.status(500).json({ error: "Failed to fetch data" });
    }
});

app.listen(PORT, () => {
    console.log(`QSTATE API running on http://localhost:${PORT}`);
});
