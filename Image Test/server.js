const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const OpenAI = require('openai');

// Load environment variables
dotenv.config();

const app = express();
const port = 3000;

// Enable CORS and JSON parsing
app.use(cors());
app.use(express.json({ limit: '10mb' })); // Allow large payloads for images

const apiKey = process.env.GITHUB_TOKEN; // Ensure this is set in your .env file
const endpoint = "https://models.inference.ai.azure.com";
const modelName = "gpt-4o";

const client = new OpenAI({
    baseURL: endpoint,
    apiKey: apiKey,
});

// API route to process image input
app.post('/api/generate', async (req, res) => {
    const { image } = req.body; // Receive the Base64-encoded image

    if (!image) {
        return res.status(400).json({ error: 'No image provided' });
    }

    try {
        // Call the GPT-4o model with the image URL and metadata
        const response = await client.chat.completions.create({
            messages: [
                { role: 'system', content: 'You are a helpful assistant that describes images in details.' },
                {
                    role: 'user',
                    content: [
                        { type: 'text', text: 'What’s in this image?' },
                        {
                            type: 'image_url',
                            image_url: {
                                url: image, // Pass the Base64-encoded image as a data URL
                                details: 'low', // Specify level of detail required
                            },
                        },
                    ],
                },
            ],
            model: modelName,
        });

        res.json({ reply: response.choices[0].message.content });
    } catch (err) {
        console.error('Error during GPT processing:', err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
