"use client";

import Link from "next/link";
import Image from "next/image";
import { useEffect, useRef } from "react";

const FeatureSection = () => {
  // const videoRef = useRef<HTMLVideoElement>(null);

  // useEffect(() => {
  //   if (videoRef.current) {
  //     videoRef.current.play().catch(error => {
  //       console.error("Error playing the video:", error);
  //     });
  //   }
  // }, []);

  return (
    <section className="py-8 md:py-12 lg:py-16 bg-background" id="features">
      <div className="main-container">
        <div className="text-center mb-16">
          <h2 className="text-xl md:text-3xl font-bold mb-2 text-[#B7A187]">Features</h2>
          <h3 className="text-2xl font-bold text-foreground mt-4 lg:mt-8 px-4 lg:px-16">
            Cross-platform Collaboration
            Facilitate interoperability between different trading platforms, allowing agents to collaborate and exchange data seamlessly.
          </h3>
        </div>

        {/* <div className="grid grid-cols-1 md:grid-cols-2 gap-10 items-center mb-20">
          <div className="bg-black rounded-xl overflow-hidden aspect-video relative">
            <video
              ref={videoRef}
              autoPlay
              loop
              muted
              playsInline
              className="w-full h-full object-cover"
            >
              <source src="https://ext.same-assets.com/4122264722/1254472206.mp4" type="video/mp4" />
            </video>
          </div>
          <div>
            <div className="code-block rounded-xl mb-6 overflow-x-auto">
              <pre className="text-sm md:text-base p-4 md:p-6">
                <code>
                  <span className="text-muted-foreground">1</span> <span className="text-blue-400">from</span> tavily <span className="text-blue-400">import</span> TavilyClient {"\n"}
                  <span className="text-muted-foreground">2</span> tavily_client = TavilyClient(api_key=<span className="text-green-400">"tvly-YOUR_API_KEY"</span>) {"\n"}
                  <span className="text-muted-foreground">3</span> response = tavily_client.search(<span className="text-green-400">"Who is Leo Messi?"</span>) {"\n"}
                  <span className="text-muted-foreground">4</span> <span className="text-blue-400">print</span>(response)
                </code>
              </pre>
            </div>
          </div>
        </div> */}

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-8">
          <div className="glass-card !bg-primary/20 p-8 flex flex-col">
            <div className="flex items-center mb-4">
              <div className="mr-4">
                <Image
                  src="https://ext.same-assets.com/4122264722/1248550479.svg"
                  alt="Real-time web access"
                  width={40}
                  height={40}
                />
              </div>
              <h3 className="text-xl font-bold text-foreground">Agent Ecosystem</h3>
            </div>
            <p className="text-muted-foreground mb-6">
              Our MCP Server coordinator as an open platform, allowing other developers or traders to access their own AI Agents and form a "market" for trading agents.
            </p>
            <div className="mt-auto">
              <Link
                href="/#ecosystem"
                className="text-primary font-medium underline hover:text-primary/80"
              >
                Ecosystem
              </Link>
            </div>
          </div>

          <div className="glass-card !bg-primary/20  p-8 flex flex-col">
            <div className="flex items-center mb-4">
              <div className="mr-4">
                <Image
                  src="https://ext.same-assets.com/4122264722/1248550479.svg"
                  alt="Plug and play"
                  width={40}
                  height={40}
                />
              </div>
              <h3 className="text-xl font-bold text-foreground">Performance Analytics Dashboard</h3>
            </div>
            <p className="text-muted-foreground mb-6">
              Offer a dashboard for viewing the performance metrics and analytics of AI trading agents in real-time, helping users evaluate agent efficiency and profitability.
            </p>
            <div className="mt-auto">
              <Link
                href="/#dashboard"
                className="text-primary font-medium hover:text-primary/80 underline"
              >
                Dashboard
              </Link>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default FeatureSection;
