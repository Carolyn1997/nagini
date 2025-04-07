import HeroSection from "@/components/hero-section";
import FeatureSection from "@/components/feature-section";
import TestimonialsSection from "@/components/testimonials-section";
import StorySection from "@/components/story-section";
// import IntroSection from "@/components/intro-section";
import McpSection from "@/components/mcp-section";

export default function Home() {
  return (
    <div className="flex-1">
      {/* Hero Section */}
      <HeroSection />

      <StorySection />

      {/* <IntroSection /> */}

      <FeatureSection />

      <McpSection />

      {/* Testimonials Section */}
      <TestimonialsSection />

      {/* FAQ Section */}
      {/* <FaqSection /> */}
    </div>
  );
}
