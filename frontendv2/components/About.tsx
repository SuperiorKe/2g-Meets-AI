
import React from 'react';
import Section from './common/Section';
import { AcademicCapIcon } from '../constants';

const About: React.FC = () => {
  return (
    <Section id="about" title="About SuperiaTech Learning" className="bg-light">
      <div className="max-w-3xl mx-auto text-center">
        <AcademicCapIcon className="w-16 h-16 text-primary mx-auto mb-6" />
        <p className="text-lg text-gray-700 leading-relaxed mb-6">
          SuperiaTech Learning is revolutionizing access to education. We leverage the power of USSD technology and cutting-edge Gemini AI to deliver bite-sized learning experiences directly to any mobile phone.
        </p>
        <p className="text-lg text-gray-700 leading-relaxed mb-8">
          Our mission is to empower students and curious minds everywhere with knowledge, breaking down barriers of internet connectivity. We believe education should be accessible to all, regardless of location or device.
        </p>
        <a
          href="mailto:info@superiatech.com" // Placeholder email
          className="inline-block bg-primary hover:bg-blue-800 text-white font-semibold py-3 px-8 rounded-lg text-lg shadow-md hover:shadow-lg transition-all duration-300"
        >
          Contact Us
        </a>
        <p className="mt-4 text-sm text-gray-500">
          (For more information, you would typically link to your actual website here)
        </p>
      </div>
    </Section>
  );
};

export default About;
    