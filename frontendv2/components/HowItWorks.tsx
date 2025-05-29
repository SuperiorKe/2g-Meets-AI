
import React from 'react';
import Section from './common/Section';
import { DevicePhoneMobileIcon, ListBulletIcon, ChatBubbleLeftRightIcon, EnvelopeIcon } from '../constants';

interface StepProps {
  icon: React.ReactNode;
  title: string;
  description: string;
  stepNumber: number;
}

const Step: React.FC<StepProps> = ({ icon, title, description, stepNumber }) => (
  <div className="flex flex-col items-center text-center p-4">
    <div className="relative mb-4">
      <div className="absolute -top-2 -left-2 bg-secondary text-white rounded-full w-8 h-8 flex items-center justify-center font-bold text-sm">
        {stepNumber}
      </div>
      <div className="p-3 bg-primary-100 rounded-full text-secondary">
         {icon}
      </div>
    </div>
    <h3 className="text-lg font-semibold text-primary mb-1">{title}</h3>
    <p className="text-gray-600 text-sm leading-relaxed">{description}</p>
  </div>
);

const steps = [
  {
    icon: <DevicePhoneMobileIcon className="w-8 h-8 md:w-10 md:h-10 text-secondary" />,
    title: 'Dial & Discover',
    description: 'Simply dial *384*XYZ# on your mobile phone to access the SuperiaTech menu.',
  },
  {
    icon: <ListBulletIcon className="w-8 h-8 md:w-10 md:h-10 text-secondary" />,
    title: 'Choose Your Path',
    description: "Select 'Learn a Topic' to explore new subjects or 'Take a Quiz' to challenge yourself.",
  },
  {
    icon: <ChatBubbleLeftRightIcon className="w-8 h-8 md:w-10 md:h-10 text-secondary" />,
    title: 'Interact via USSD',
    description: "Enter your desired topic or choose a quiz category using your phone's keypad.",
  },
  {
    icon: <EnvelopeIcon className="w-8 h-8 md:w-10 md:h-10 text-secondary" />,
    title: 'Learn via SMS',
    description: 'Receive AI-generated explanations or quiz questions directly in your SMS inbox.',
  },
];

const HowItWorks: React.FC = () => {
  return (
    <Section id="how-it-works" title="Simple Steps to Start Learning" className="bg-white">
      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
        {steps.map((step, index) => (
          <Step
            key={index}
            stepNumber={index + 1}
            icon={step.icon}
            title={step.title}
            description={step.description}
          />
        ))}
      </div>
       <div className="mt-12 text-center">
        <img 
          src="https://picsum.photos/seed/howitworks/1000/400" 
          alt="USSD interaction flow" 
          className="rounded-lg shadow-xl mx-auto max-w-3xl w-full"
        />
        <p className="mt-4 text-sm text-gray-500">Illustrative representation of the USSD learning process.</p>
      </div>
    </Section>
  );
};

export default HowItWorks;
    