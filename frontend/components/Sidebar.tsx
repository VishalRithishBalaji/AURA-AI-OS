import {
  Bot,
  Brain,
  Workflow,
  Globe,
  Settings,
} from "lucide-react";

export default function Sidebar() {
  return (
    <div className="w-64 bg-zinc-950 border-r border-zinc-800 h-screen p-5">
      <div className="mb-10">
        <h1 className="text-3xl font-bold text-cyan-400">
          AURA
        </h1>
      </div>

      <div className="space-y-4">
        <SidebarItem icon={<Bot size={20} />} title="Chat" />
        <SidebarItem icon={<Brain size={20} />} title="Memory" />
        <SidebarItem icon={<Workflow size={20} />} title="Workflows" />
        <SidebarItem icon={<Globe size={20} />} title="Browser Agent" />
        <SidebarItem icon={<Settings size={20} />} title="Settings" />
      </div>
    </div>
  );
}

function SidebarItem({
  icon,
  title,
}: {
  icon: React.ReactNode;
  title: string;
}) {
  return (
    <div className="flex items-center gap-3 text-zinc-300 hover:bg-zinc-800 transition cursor-pointer p-3 rounded-xl">
      {icon}
      <span>{title}</span>
    </div>
  );
}