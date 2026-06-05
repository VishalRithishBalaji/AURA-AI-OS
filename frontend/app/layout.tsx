import "./globals.css";

export const metadata = {
  title: "AURA AI",
  description: "Autonomous Agentic AI Assistant",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}