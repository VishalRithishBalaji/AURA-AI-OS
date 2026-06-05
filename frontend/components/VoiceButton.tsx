"use client";

import { Mic } from "lucide-react";

import { sendVoice } from "@/services/api";


type Props = {
  onMessage: (
    msg: any,
    isUser?: boolean
  ) => void;
};


export default function VoiceButton({
  onMessage,
}: Props) {

  const startListening = () => {

    const SpeechRecognition =
      (window as any).SpeechRecognition ||
      (window as any).webkitSpeechRecognition;

    if (!SpeechRecognition) {

      alert(
        "Speech Recognition not supported"
      );

      return;
    }

    const recognition =
      new SpeechRecognition();

    recognition.lang = "en-US";

    recognition.continuous = false;

    recognition.interimResults = false;

    recognition.maxAlternatives = 1;


    recognition.start();


    recognition.onstart = () => {

      console.log("🎤 Listening...");
    };


    recognition.onresult = async (
      event: any
    ) => {

      try {

        const transcript =
          event.results[0][0].transcript;

        console.log(
          "🗣",
          transcript
        );

        // USER MESSAGE
        onMessage({
          role: "user",
          content: transcript,
        });

        // SEND TO BACKEND
        const data =
          await sendVoice(transcript);

        // AI MESSAGE
        onMessage({
          role: "assistant",
          content: data.response,
        });

        // SPEAK RESPONSE
        const utterance =
          new SpeechSynthesisUtterance(
            data.response
          );

        utterance.rate = 1;

        utterance.pitch = 1;

        utterance.volume = 1;

        speechSynthesis.speak(
          utterance
        );

      } catch (err) {

        console.log(
          "Voice processing error:",
          err
        );
      }
    };


    recognition.onerror = (
      event: any
    ) => {

      // IGNORE NORMAL EVENTS
      if (
        event.error === "no-speech" ||
        event.error === "aborted"
      ) {

        console.log(
          "Voice idle..."
        );

        return;
      }

      console.log(
        "Speech error:",
        event.error
      );
    };


    recognition.onend = () => {

      console.log(
        "🎤 Voice recognition ended"
      );
    };
  };


  return (

    <button
      onClick={startListening}

      className="
      bg-cyan-500
      hover:bg-cyan-400
      transition
      p-4
      rounded-2xl
      "
    >

      <Mic className="text-white" />

    </button>
  );
}