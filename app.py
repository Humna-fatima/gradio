import gradio as gr
import requests

API = "http://localhost:8000"

def get_all_items():
    res = requests.get(f"{API}/items/")
    return res.json()

with gr.Blocks() as demo:
    gr.Markdown("## My App")
    btn = gr.Button("Load data")
    output = gr.JSON()
    btn.click(get_all_items, outputs=output)

demo.launch(server_port=7860)   #we can leave empty this port thing as well 