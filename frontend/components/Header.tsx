export default function Header() {
  return (
    <div className="h-16 border-b border-zinc-800 flex items-center justify-between px-6 bg-zinc-950">
      <div>
        <h1 className="text-2xl font-bold text-cyan-400">
          AURA AI
        </h1>
      </div>

      <div className="text-sm text-zinc-400">
        Autonomous Agentic Assistant
      </div>
    </div>
  );
}