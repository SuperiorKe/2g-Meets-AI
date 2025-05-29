
import React from 'react';
import Section from './common/Section';

const Hero: React.FC = () => {
  const scrollToFeatures = (e: React.MouseEvent<HTMLAnchorElement>) => {
    e.preventDefault();
    const featuresSection = document.getElementById('features');
    if (featuresSection) {
      featuresSection.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <Section id="hero" className="bg-gradient-to-br from-primary to-blue-700 text-white min-h-[calc(100vh-5rem)] flex items-center">
      <div className="text-center">
        <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold mb-6 leading-tight">
          Unlock Knowledge, <span className="text-secondary">Offline</span>.
        </h1>
        <p className="text-lg sm:text-xl md:text-2xl text-blue-100 mb-10 max-w-3xl mx-auto">
          SuperiaTech Learning delivers AI-powered education via simple USSD codes. Learn anytime, anywhere—no internet needed.
        </p>
        <div className="space-y-4 sm:space-y-0 sm:space-x-6">
          <a
            href="#features"
            onClick={scrollToFeatures}
            className="inline-block bg-secondary hover:bg-emerald-500 text-white font-semibold py-3 px-8 rounded-lg text-lg shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-105"
          >
            Discover Features
          </a>
          <div className="mt-6 md:mt-8">
            <p className="text-blue-200 text-sm">Ready to start learning?</p>
            <p className="text-white font-mono text-xl md:text-2xl bg-black bg-opacity-20 px-4 py-2 rounded-md inline-block mt-2">
              Dial <span className="text-secondary font-bold">*789*9800#</span>
            </p>
          </div>
        </div>
      </div>
      {/* Placeholder for a potential image or graphic if desired later */}
      {/* <div className="mt-12 max-w-3xl mx-auto">
        <img src="https://picsum.photos/800/400?grayscale&blur=2" alt="Abstract learning" className="rounded-lg shadow-xl"/>
      </div> */}
    </Section>
  );
};

export default Hero;
    