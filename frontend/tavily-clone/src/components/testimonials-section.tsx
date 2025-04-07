"use client";

import Image from "next/image";
import { Card, CardContent } from "@/components/ui/card";
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel";

const testimonials = [
  {
    quote: "Accurate and up-to-date knowledge has become a key component of building many types of LLM-powered apps. Tavily's reliable search APIs have made them an essential partner for LangChain, and our open-source integration with them has been a huge boon to the community as a whole. It's always a pleasure working with the Tavily team!",
    author: "Jacob Lee",
    role: "Founding Engineer at Langchain",
    avatar: "https://github.com/identicons/jazzicon-1.png",
  },
  {
    quote: "We've been using Tavily's Search API to power Athena, our Enterprise AI Data Analyst. The ability to retrieve accurate, real-time information tailored for AI agents has significantly enhanced Athena's research capabilities. Tavily's focus on delivering factual and explicit results aligns perfectly with our commitment to providing trustworthy and sourced insights to our enterprise clients.",
    author: "Brendon Geils",
    role: "Co-Founder of Athena Intelligence",
    avatar: "https://github.com/identicons/jazzicon-2.png",
  },
];

const userFeedback = [
  {
    quote: "When it comes to producing quality reports, it is important to have accurate and up-to-date information as input. That's why I recommended Tavily for your next research.",
    author: "Amine Izrizar",
    handle: "@izrizar-amine",
    platform: "linkedin",
    avatar: "https://github.com/identicons/jazzicon-3.png",
  },
  {
    quote: "I was recommended to try Tavily REST API GPT search engine - and it was amazing and very easy to set up.",
    author: "Audi Previo",
    handle: "@audi-previo",
    platform: "linkedin",
    avatar: "https://github.com/identicons/jazzicon-4.png",
  },
  {
    quote: "Connected to the web, to provide the data real time, the best consistent connection can be achieved with the help of Tavily.",
    author: "Hrishikesh Yadav",
    handle: "@hrishikesh_ai",
    platform: "twitter",
    avatar: "https://github.com/identicons/jazzicon-5.png",
  },
  {
    quote: "Tavily is doing such a fantastic job in this space, they deserve recognition.",
    author: "Pinaki Bhattacharyya",
    handle: "@pinaki-bhattacharyya",
    platform: "linkedin",
    avatar: "https://github.com/identicons/jazzicon-6.png",
  },
];

const TestimonialsSection = () => {
  return (
    <section className="py-8 md:py-12 lg:py-16 bg-background" id="testimonials">
      <div className="main-container">
        <div className="text-center mb-16">
          <h2 className="text-xl md:text-3xl font-bold mb-2 text-[#B7A187]">Testimonials</h2>
          <h3 className="text-2xl font-bold text-foreground mt-4 lg:mt-8 px-4 lg:px-16">
            Nagini is trusted by AI leaders around the world
          </h3>
        </div>

        {/* Testimonials Skeleton */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-20">
          {[1, 2].map((item) => (
            <div
              key={item}
              className="glass-card p-8 hover:shadow-lg transition-all duration-300 flex flex-col"
            >
              {/* Quote skeleton */}
              <div className="flex-1 mb-6 space-y-3">
                <div className="h-4 bg-gray-200 rounded w-3/4"></div>
                <div className="h-4 bg-gray-200 rounded w-full"></div>
                <div className="h-4 bg-gray-200 rounded w-2/3"></div>
              </div>
              
              {/* Author info skeleton */}
              <div className="flex items-center">
                <div className="mr-4">
                  <div className="w-[50px] h-[50px] rounded-full bg-gray-200 "></div>
                </div>
                <div className="space-y-2">
                  <div className="h-4 bg-gray-200 rounded w-32"></div>
                  <div className="h-3 bg-gray-200 rounded w-24"></div>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* What our users say */}
        <div className="mb-16 hidden">
          <h3 className="text-2xl font-bold mb-8 text-center">What our users say</h3>

          <Carousel className="w-full">
            <CarouselContent>
              {userFeedback.map((item, index) => (
                <CarouselItem key={index} className="md:basis-1/2 lg:basis-1/3 h-full">
                  <Card>
                    <CardContent className="p-6">
                      <div className="mb-4">
                        <p className="text-gray-600">"{item.quote}"</p>
                      </div>
                      <div className="flex items-center">
                        <div className="mr-3">
                          <Image
                            src={item.avatar}
                            alt={item.author}
                            width={40}
                            height={40}
                            className="rounded-full"
                          />
                        </div>
                        <div>
                          <h4 className="font-bold text-sm">{item.author}</h4>
                          <div className="flex items-center">
                            <span className="text-gray-500 text-xs">{item.handle}</span>
                            <Image
                              src={item.platform === "twitter"
                                ? "https://ext.same-assets.com/4122264722/3695124275.svg"
                                : "https://ext.same-assets.com/4122264722/3661595502.svg"
                              }
                              alt={item.platform}
                              width={14}
                              height={14}
                              className="ml-1 w-3 h-3"
                            />
                          </div>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </CarouselItem>
              ))}
            </CarouselContent>
            <div className="flex justify-center mt-6">
              <CarouselPrevious className="static mr-2 translate-y-0" />
              <CarouselNext className="static ml-2 translate-y-0" />
            </div>
          </Carousel>
        </div>
      </div>
    </section>
  );
};

export default TestimonialsSection;
