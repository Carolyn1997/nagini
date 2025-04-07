const IntroSection = () => {
  return (
    <section className="py-8 md:py-12 lg:py-16 bg-background" id="intro">
      <div className="main-container">
        <div className="text-center mb-16">
          <h2 className="text-xl md:text-3xl font-bold mb-2 text-[#B7A187]">Introducing Nagini</h2>
          <h3 className="text-2xl font-bold text-foreground mt-4 lg:mt-8 px-4 lg:px-16">
          AI-powered quant agent slithering through crypto markets. Precision trading, data-driven insights, and serpentine strategies.
          </h3>
        </div>

        {/* <div className="glass-card p-8 md:p-10 relative overflow-hidden">
          <div className="relative z-10">
            <h2 className="text-2xl md:text-3xl font-bold mb-4 text-foreground">
              Discover the Power of AI with Tavily's Advanced Search Capabilities
            </h2>
            <p className="mb-6 text-muted-foreground md:max-w-2xl">
              Tavily's AI-driven approach handles the heavy lifting, providing you with precise, real-time information so you can focus on what truly matters.
            </p>
            <div className="flex flex-col sm:flex-row gap-4">
              <Link href="https://docs.tavily.com/">
                <Button variant="outline" className="border-primary/20 text-primary hover:bg-primary/10">
                  Learn More
                </Button>
              </Link>
              <Link href="mailto:support@tavily.com">
                <Button className="bg-primary hover:bg-primary/90">
                  Contact Us
                </Button>
              </Link>
            </div>
          </div>
          <div className="absolute right-0 bottom-0 w-full h-full overflow-hidden">
            <Image
              src="https://ext.same-assets.com/4122264722/2578548711.svg"
              alt="Background pattern"
              fill
              className="object-cover opacity-10"
            />
          </div>
        </div> */}
      </div>
    </section>
  );
};

export default IntroSection;
