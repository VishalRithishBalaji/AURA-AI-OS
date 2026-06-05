import Sidebar from "@/components/Sidebar";
import ChatBox from "@/components/ChatBox";
import Header from "@/components/Header";

export default function HomePage() {
  return (
    <main className="flex bg-black text-white min-h-screen">
      <Sidebar />

      <div className="flex-1 flex flex-col">
        <Header />

        <ChatBox />
      </div>
    </main>
  );
}