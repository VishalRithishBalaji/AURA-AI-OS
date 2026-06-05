"use client";

import { useState } from "react";

import { Send } from "lucide-react";

import { useChat } from "@/hooks/useChat";

import MessageBubble from "./MessageBubble";

import VoiceButton from "./VoiceButton";


export default function ChatBox() {

  const [input, setInput] = useState("");

  const {
    messages,
    send,
    addMessage,
  } = useChat();


  const handleSend = async () => {

    if (!input.trim()) return;

    await send(input);

    setInput("");
  };


  return (

    <div className="flex flex-col h-screen bg-zinc-900">

      {/* CHAT AREA */}
      <div className="flex-1 overflow-y-auto p-6">

        {messages.length === 0 && (

          <div className="h-full flex items-center justify-center">

            <div className="text-center">

              <h1 className="
                text-5xl
                font-bold
                text-cyan-400
                mb-4
              ">
                AURA AI
              </h1>

              <p className="
                text-zinc-400
                text-lg
              ">
                Your Autonomous Agentic AI Assistant
              </p>

            </div>

          </div>
        )}


        {messages.map((msg, index) => (

          <MessageBubble
            key={index}
            role={msg.role}
            content={msg.content}
          />

        ))}

      </div>


      {/* INPUT AREA */}
      <div className="
        border-t
        border-zinc-800
        p-5
        bg-zinc-950
      ">

        <div className="
          flex
          gap-3
          items-center
        ">

          {/* TEXT INPUT */}
          <input
            type="text"
            value={input}
            onChange={(e) =>
              setInput(e.target.value)
            }

            onKeyDown={(e) => {

              if (e.key === "Enter") {

                handleSend();
              }
            }}

            placeholder="Ask AURA AI anything..."

            className="
              flex-1
              bg-zinc-800
              text-white
              px-5
              py-4
              rounded-2xl
              outline-none
              border
              border-zinc-700
              focus:border-cyan-500
            "
          />


          {/* VOICE BUTTON */}
          <VoiceButton
            onMessage={addMessage}
          />


          {/* SEND BUTTON */}
          <button
            onClick={handleSend}

            className="
              bg-cyan-500
              hover:bg-cyan-400
              transition
              p-4
              rounded-2xl
            "
          >

            <Send className="text-white" />

          </button>

        </div>

      </div>

    </div>
  );
}