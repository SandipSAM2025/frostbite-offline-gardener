# 🌿 FrostBite: Offline Open-Weight Garden Scout

> **Hacktoberfest 2026 — Week 1: Touch Grass Challenge**  
> A lightweight, zero-cloud CLI tool that pairs local frost benchmark data with an on-device open SLM (`smollm2:1.7b`) to give you a 5-step physical outdoor gardening card in under 3 seconds.

---

## 📖 Overview

Most generative AI tools encourage endless conversational screen time. **FrostBite** flips that script:

- Runs **100% offline** on your machine — no internet required.  
- Accepts your **hardiness zone or region** and looks up historical frost benchmark dates locally.  
- Prompts a locally running lightweight SLM with strict constraints to output concise, actionable chores.  
- Renders an **ASCII index-card format** directly in your terminal and saves `garden_todo.txt` so you can fold the slip, pocket a pencil, close your laptop, and head outdoors.  

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+  
- **Inference Engine:** [Ollama](https://ollama.com) (local loopback at `http://localhost:11434`)  
- **Model:** `smollm2:1.7b` (Hugging Face / Ollama) — ultra-compact 1.7B parameter open-weight model designed for fast, local CPU/RAM inference  
- **Dependencies:** `requests` (for local REST communication)  

---

## 🚀 Quickstart

### 1. Prerequisites
Install [Ollama](https://ollama.com) and ensure it is running locally.

### 2. Pull the Open-Weight Model
Run the following in your terminal to fetch the lightweight model (~1 GB):

```bash
ollama run smollm2:1.7b
