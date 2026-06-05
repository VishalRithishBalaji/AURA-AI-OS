"use client";

import { useChatStore } from "@/store/chatStore";

import { sendMessage } from "@/services/api";

export const useChat = () => {

  const {
    messages,
    addMessage,
  } = useChatStore();

  const send = async (
    text: string
  ) => {

    // USER MESSAGE
    addMessage({
      role: "user",
      content: text,
    });

    try {

      // SEND TO BACKEND
      const data =
        await sendMessage(text);

      // AI MESSAGE
      addMessage({
        role: "assistant",
        content: data.response,
      });

    } catch (err) {

      addMessage({
        role: "assistant",
        content:
          "Error connecting to AURA backend.",
      });

      console.error(err);
    }
  };

  return {
    messages,
    send,
    addMessage,
  };
};
