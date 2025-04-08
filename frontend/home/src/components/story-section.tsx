"use client";

import { motion } from "framer-motion";
import { useInView } from "framer-motion";
import { useRef } from "react";

const StorySection = () => {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-100px" });

  return (
    <section className="py-8 md:py-12 lg:py-16 bg-background" id="approach" ref={ref}>
      <div className="main-container">
        <motion.div 
          className="text-center mb-16"
          initial={{ opacity: 0, scale: 0.9 }}
          animate={isInView ? { opacity: 1, scale: 1 } : { opacity: 0, scale: 0.9 }}
          transition={{ duration: 0.8 }}
        >
          <motion.h2 
            className="text-xl md:text-3xl font-bold mb-2 text-[#B7A187]"
            initial={{ opacity: 0, y: -20 }}
            animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: -20 }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            Story
          </motion.h2>
          <motion.h3 
            className="text-2xl font-bold text-foreground mt-4 lg:mt-8 px-4 lg:px-16"
            initial={{ opacity: 0, y: 20 }}
            animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 20 }}
            transition={{ duration: 0.6, delay: 0.4 }}
          >
            Our AI Quant Trading Agent no longer just executes strategies, but connects to the global financial pulse through MCP Server, adjusts strategies in real time, and transcends the limitations of traditional quantitative trading.
          </motion.h3>
        </motion.div>
      </div>
    </section>
  );
};

export default StorySection;
