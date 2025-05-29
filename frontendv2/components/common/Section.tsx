
import React from 'react';

interface SectionProps {
  id: string;
  title?: string;
  children: React.ReactNode;
  className?: string;
  titleClassName?: string;
  contentClassName?: string;
}

const Section: React.FC<SectionProps> = ({ id, title, children, className = '', titleClassName = '', contentClassName = '' }) => {
  return (
    <section id={id} className={`py-16 md:py-24 px-4 sm:px-6 lg:px-8 ${className}`}>
      <div className="max-w-7xl mx-auto">
        {title && (
          <h2 className={`text-3xl md:text-4xl font-bold text-center text-primary mb-12 md:mb-16 ${titleClassName}`}>
            {title}
          </h2>
        )}
        <div className={contentClassName}>
          {children}
        </div>
      </div>
    </section>
  );
};

export default Section;
    