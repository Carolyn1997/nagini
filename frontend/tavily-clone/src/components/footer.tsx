import Image from "next/image";
import { Button } from "@/components/ui/button";
import Link from "next/link";
import { Twitter, Github, Send } from "lucide-react";
import { TradingRecord } from "./trading-record";

const Footer = () => {
  return (
    <footer id="footer" className="relative py-12">
      <div className="main-container">
        <div className="relative rounded-2xl bg-gradient-to-br from-primary/10 to-secondary shadow-[0_0_40px_rgba(0,0,0,0.1)] hover:shadow-[0_0_50px_rgba(0,0,0,0.15)] transition-all duration-500 overflow-hidden transform hover:-translate-y-1">
          <div className="absolute inset-0 bg-grid-white opacity-10" />
          <div className="relative z-10">
            {/* Main content section */}
            <div className="p-8 md:p-12">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                {/* Left side content */}
                <div className="flex flex-col items-start">
                  <h2 className="text-2xl md:text-3xl font-bold mb-2 text-foreground">
                    Ready to get started?
                  </h2>
                  <p className="text-muted-foreground mb-8">
                    Unleash the power of AI-driven quantitative trading in crypto markets.
                  </p>
                  <div className="flex flex-col sm:flex-row gap-4 mb-8">
                    <Link href="https://t.me/carolyn_1197" target="_blank" rel="noopener noreferrer">
                      <Button variant="outline" className="border-primary/20 text-primary hover:bg-primary/10 backdrop-blur-sm rounded-full px-8">
                        Join the community
                      </Button>
                    </Link>
                    <Button className="bg-primary hover:bg-primary/90 shadow-lg hover:shadow-primary/25 rounded-full px-8">
                      Get Started
                    </Button>
                  </div>

                  {/* Social media links */}
                  <div className="flex gap-4">
                    <a href="https://x.com/nagini_ai" target="_blank" rel="noopener noreferrer" className="text-muted-foreground hover:text-primary transition-colors">
                      <Twitter size={20} />
                    </a>
                    <a href="https://github.com/Carolyn1997/nagini.git" target="_blank" rel="noopener noreferrer" className="text-muted-foreground hover:text-primary transition-colors">
                      <Github size={20} />
                    </a>
                    <a href="https://t.me/carolyn_1197" target="_blank" rel="noopener noreferrer" className="text-muted-foreground hover:text-primary transition-colors">
                      <Send size={20} />
                    </a>
                  </div>
                </div>

                {/* Right side trading record */}
                <div className="relative h-[300px]">
                  <TradingRecord />
                </div>
              </div>

              {/* Footer bottom */}
              <div className="mt-12 pt-8 border-t border-primary/20">
                <div className="flex flex-col md:flex-row justify-between items-center">
                  <div className="text-muted-foreground text-sm mb-4 md:mb-0">
                    <span>Designed by </span>
                    <a
                      href="https://peppermint.id/"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="hover:text-primary transition-colors"
                    >
                      <span className="sr-only">Peppermint</span>
                      <Image
                        src="/logo.jpg"
                        alt="Peppermint"
                        width={18}
                        height={18}
                        className="inline-block h-4 w-auto mx-1"
                      />
                    </a>
                    <span> 2025 Nagini.</span>
                  </div>
                  <div className="text-muted-foreground text-sm">
                    <a href="https://t.me/carolyn_1197" className="hover:text-primary transition-colors">
                      Carolyn@nagini.ai
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Enhanced background effects */}
          <div className="absolute inset-0 bg-gradient-to-tr from-background/50 via-secondary/50 to-background/50" />
          <div className="absolute inset-0 w-full h-full">
            <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-background to-transparent backdrop-blur-[1px]" />
            <div className="absolute top-0 left-0 right-0 h-32 bg-gradient-to-b from-background to-transparent backdrop-blur-[1px]" />
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
