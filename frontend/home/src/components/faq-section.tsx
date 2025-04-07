"use client";

import Link from "next/link";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";

const faqItems = [
  {
    question: "What is Tavily Search API?",
    answer: "Tavily Search API is a specialized search engine designed for Large Language Models (LLMs) and AI agents. It provides real-time, accurate, and unbiased information, enabling AI applications to retrieve and process data efficiently. Tavily is built with AI developers in mind, simplifying the process of integrating dynamic web information into AI-driven solutions."
  },
  {
    question: "How does Tavily differ from other search APIs?",
    answer: "Unlike Bing, Google and SerpAPI, Tavily Search API reviews multiple sources to find the most relevant content from each source, delivering concise, ready-to-use information optimized for LLM context. This focus on RAG and LLMs ensures your AI applications access only the highest-quality data. Tavily Search API is also more affordable and flexible."
  },
  {
    question: "What are the key features of Tavily?",
    answer: (
      <>
        <ul className="list-disc pl-6 space-y-2 mt-2">
          <li>Purpose-built for AI: Designed with AI agents and LLMs in mind, ensuring ideal results for AI workflows like Retrieval Augmented Generation (RAG).</li>
          <li>Customizable: Control the search depth, manage domains.</li>
          <li>Real-time: Retrieves reliable, up-to-date information, ensuring your AI systems have the most relevant data.</li>
          <li>Easy Integration: Simple API setup with support for Python libraries and partnerships with LangChain and LlamaIndex.</li>
          <li>Scalable: Tavily is built to scale as your usage grows, making it a reliable solution for both startups and enterprise customers.</li>
        </ul>
      </>
    )
  },
  {
    question: "How does Tavily ensure the accuracy of the information it provides?",
    answer: "Tavily employs advanced algorithms and NLP techniques to gather information from trusted, authoritative sources. This guarantees the information is relevant, accurate, and verifiable. Additionally, users can prioritize preferred sources to enhance the relevance of the search results."
  },
  {
    question: "How fast is Tavily's search API?",
    answer: "Speed is a top priority for Tavily. The API typically returns results within seconds (or less!), although complex queries involving extensive data processing may take slightly longer. The system is optimized for efficiency without sacrificing the quality of information."
  },
  {
    question: "Is there a free plan available?",
    answer: "Yes! Tavily offers a free plan that includes limited monthly API calls. This allows you to test its capabilities and explore how it fits into your AI projects before committing to a paid subscription. No credit card is required for the free plan."
  },
  {
    question: "Does Tavily provide citations for the information it retrieves?",
    answer: "Yes, Tavily is committed to transparency. The API includes citations for all the information it retrieves, ensuring you know exactly where the data comes from."
  },
  {
    question: "What is GPT Researcher and how does it relate to Tavily?",
    answer: "GPT Researcher is an open-source, autonomous agent powered by Tavily's Search API. It automates the research process by retrieving, filtering, and synthesizing data from over 20 web sources per task. This simplifies and accelerates information gathering, making it a valuable tool for anyone needing quick and thorough research."
  },
  {
    question: "What kind of support does Tavily provide?",
    answer: (
      <>
        <ul className="list-disc pl-6 space-y-2 mt-2">
          <li>Paid subscriptions: Email support via <a href="mailto:support@tavily.com" className="text-primary hover:underline">support@tavily.com</a></li>
          <li>Enterprise Plan: Dedicated, white-glove support with a personal Slack channel, an account manager, an AI engineer for technical assistance, and regular check-ins. We help with debugging, best practices for agent workflows, Retrieval-Augmented Generation (RAG) techniques, and architecture reviews.</li>
        </ul>
      </>
    )
  },
  {
    question: "When do my API credits reset?",
    answer: "Your API credits reset on the first day of each month, regardless of the billing date. This ensures you start each month with a clean slate of credits to use for your searches."
  },
  {
    question: "How does Tavily handle data privacy?",
    answer: <span>Our <Link href="/privacy" className="text-primary hover:underline">privacy policy</Link> outlines how we handle and protect user data, ensuring full compliance with global data regulations.</span>
  },
];

const FaqSection = () => {
  return (
    <section className="py-8 md:py-12 lg:py-16 bg-background" id="faq">
      <div className="main-container">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-3xl font-bold mb-2 text-foreground">Faq</h2>
            <h3 className="text-3xl font-bold mb-4 text-foreground">Everything you need to know</h3>
            <p className="text-muted-foreground">
              If you have any questions, please do not hesitate to reach to our support team.
              <Link
                href="mailto:support@tavily.com"
                className="text-primary font-medium hover:underline ml-1"
              >
                Contact Us
              </Link>
            </p>
          </div>

          <Accordion type="single" collapsible className="space-y-4">
            {faqItems.map((item, i) => (
              <AccordionItem
                key={`faq-${i}`}
                value={`faq-${i}`}
                className="glass-card border-primary/20"
              >
                <AccordionTrigger className="px-6 py-4 text-lg font-medium text-foreground">
                  {item.question}
                </AccordionTrigger>
                <AccordionContent className="px-6 pb-6 text-muted-foreground">
                  {item.answer}
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </div>
    </section>
  );
};

export default FaqSection;
