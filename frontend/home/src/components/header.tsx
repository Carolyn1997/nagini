"use client";

import { useState } from "react";
import Link from "next/link";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { Button } from "@/components/ui/button";
import { Menu, X } from "lucide-react";

const navLinks = [
  { name: "Story", href: "/#story" },
  { name: "Features", href: "/#features" },
  { name: "Mcp", href: "/#mcp" },
  { name: "Join", href: "/#footer" },
];

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <header className="sticky top-4 z-50 w-full border-border/50 bg-background/95 backdrop-blur-sm">
      <div className="main-container py-2">
        <div className="bg-background/50 rounded-2xl shadow-lg border border-border/50 backdrop-blur-sm mx-auto flex items-center justify-between h-16 px-6">
          {/* Logo */}
          {/* <Link href="/" className="flex items-center">
            <Image
              src="/logo.jpg"
              alt="Logo"
              width={120}
              height={40}
              className="h-8 w-auto"
            />
          </Link> */}
          <Link href="/#hero" className="flex items-center">
            <h1 className="text-primary font-bold text-2xl">NAGINI</h1>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center">
            {navLinks.map((link) => (
              <Link
                key={link.name}
                href={link.href}
                className="px-4 py-2 text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
              >
                {link.name}
              </Link>
            ))}
          </nav>

          {/* Status and Auth Links */}
          <div className="hidden md:flex items-center gap-4">
            {/* <div className="flex items-center gap-1 text-emerald-600">
              <span className="h-2 w-2 bg-emerald-500 rounded-full" />
              <span className="text-xs font-medium">Operational</span>
            </div> */}
            <Button className="rounded-full bg-primary text-primary-foreground hover:bg-primary/90">Log In</Button>
          </div>

          {/* Mobile Menu */}
          <Sheet open={isMenuOpen} onOpenChange={setIsMenuOpen}>
            <SheetTrigger asChild className="md:hidden">
              <Button variant="ghost" className="p-0 h-9 w-9" onClick={() => setIsMenuOpen(true)}>
                {isMenuOpen ? (
                  <X className="h-5 w-5" />
                ) : (
                  <Menu className="h-5 w-5" />
                )}
                <span className="sr-only">Toggle menu</span>
              </Button>
            </SheetTrigger>
            <SheetContent side="right" className="w-[300px] sm:w-[380px] pt-10 bg-background/95 backdrop-blur-sm">
              <nav className="flex flex-col gap-4">
                {navLinks.map((link) => (
                  <Link
                    key={link.name}
                    href={link.href}
                    className="px-3 py-2 text-base font-medium text-muted-foreground hover:text-primary hover:bg-secondary/50 rounded-md"
                    onClick={() => setIsMenuOpen(false)}
                  >
                    {link.name}
                  </Link>
                ))}
                <div className="mt-4 pt-4 border-t border-border">
                  {/* <Link
                    href="https://status.tavily.com/"
                    className="px-3 py-2 text-base font-medium text-muted-foreground hover:text-primary hover:bg-secondary/50 rounded-md flex items-center"
                    onClick={() => setIsMenuOpen(false)}
                  >
                    <span className="h-2 w-2 bg-emerald-500 rounded-full mr-2" />
                    Operational
                  </Link> */}
                  <Button className="mt-4 w-full bg-primary hover:bg-primary/90 rounded-full">
                    Log In
                  </Button>
                </div>
              </nav>
            </SheetContent>
          </Sheet>
        </div>
      </div>
    </header>
  );
};

export default Header;
