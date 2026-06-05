"use client";

import ReactMarkdown from "react-markdown";

type Props = {
  role: string;
  content: string;
};

export default function MessageBubble({
  role,
  content,
}: Props) {

  const isUser = role === "user";

  return (

    <div
      className={`
      mb-6
      flex
      ${isUser ? "justify-end" : "justify-start"}
      `}
    >

      <div
        className={`
        max-w-3xl
        px-5
        py-4
        rounded-2xl
        whitespace-pre-wrap
        leading-7

        ${
          isUser
            ? "bg-cyan-500 text-white"
            : "bg-zinc-800 text-zinc-100"
        }
        `}
      >

        <ReactMarkdown>
          {
            typeof content === "string"
              ? content
              : JSON.stringify(
                  content,
                  null,
                  2
                )
          }
        </ReactMarkdown>

      </div>

    </div>
  );
}