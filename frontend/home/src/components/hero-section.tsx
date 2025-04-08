"use client";

import Image from "next/image";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

const HeroSection = () => {
  // const videoRef = useRef<HTMLVideoElement>(null);

  // useEffect(() => {
  //   if (videoRef.current) {
  //     videoRef.current.play().catch(error => {
  //       console.error("Error playing the video:", error);
  //     });
  //   }
  // }, []);

  return (
    <section id="hero" className="relative hero-gradient py-16 md:py-24 overflow-hidden">
      <div className="main-container relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          {/* Left content */}
          <div className="flex flex-col items-start lg:items-center text-left">
            <motion.h1 
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8 }}
              className="text-4xl md:text-5xl lg:text-6xl font-bold mb-6 tracking-tight text-gray-900"
            >
              NAGINI
              <br />
              Ecosystem
            </motion.h1>
            <motion.p 
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="text-lg text-gray-600 mb-8 max-w-xl"
            >
              AI-driven trading platform
            </motion.p>
            <motion.div 
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.4 }}
              className="flex flex-col sm:flex-row gap-4"
            >
              <Button variant="outline" size="lg" className="rounded-full">
                Learn More
              </Button>
              <Button size="lg" className="bg-gray-900 hover:bg-gray-800 rounded-full">
                Get Started
              </Button>
            </motion.div>

            <div className="mt-16 hidden">
              <p className="text-sm text-gray-500 mb-4">
                Trusted by AI leaders around the world
              </p>
              <div className="flex flex-wrap gap-8 mt-2">
                <Image
                  src="https://ext.same-assets.com/4122264722/2118624581.svg"
                  alt="SimilarWeb"
                  width={120}
                  height={40}
                  className="h-6 w-auto opacity-70"
                />
                <Image
                  src="https://ext.same-assets.com/4122264722/1173849394.svg"
                  alt="LangChain"
                  width={120}
                  height={40}
                  className="h-6 w-auto opacity-70"
                />
                <Image
                  src="https://ext.same-assets.com/4122264722/2345857269.svg"
                  alt="Athena"
                  width={120}
                  height={40}
                  className="h-6 w-auto opacity-70"
                />
              </div>
            </div>
          </div>

          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 1, delay: 0.6 }}
          >
            <Image
              src="/logo.jpg"
              alt="Nagini Logo"
              width={800}
              height={800}
              className="w-full h-auto"
              priority
            />
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
