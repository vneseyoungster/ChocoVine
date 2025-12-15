/**
 * Component Template
 *
 * Copy this template when creating new React components.
 * Adjust based on component complexity and requirements.
 */

import React, { useState, useCallback, useMemo } from 'react';

// ============================================================================
// Types
// ============================================================================

/**
 * Props interface for ComponentName
 */
interface ComponentNameProps {
  /** Required prop description */
  requiredProp: string;

  /** Optional prop with default */
  optionalProp?: number;

  /** Optional variant */
  variant?: 'primary' | 'secondary';

  /** Optional size */
  size?: 'sm' | 'md' | 'lg';

  /** Optional disabled state */
  disabled?: boolean;

  /** Optional click handler */
  onClick?: () => void;

  /** Optional children */
  children?: React.ReactNode;

  /** Optional className for styling overrides */
  className?: string;
}

// ============================================================================
// Constants
// ============================================================================

const DEFAULT_SIZE = 'md';
const DEFAULT_VARIANT = 'primary';

// ============================================================================
// Helpers
// ============================================================================

/**
 * Generate class names based on props
 */
function getClassNames(
  variant: string,
  size: string,
  disabled: boolean,
  className?: string
): string {
  const classes = [
    'component-name',
    `component-name--${variant}`,
    `component-name--${size}`,
  ];

  if (disabled) {
    classes.push('component-name--disabled');
  }

  if (className) {
    classes.push(className);
  }

  return classes.join(' ');
}

// ============================================================================
// Component
// ============================================================================

/**
 * ComponentName
 *
 * Brief description of what this component does and when to use it.
 *
 * @example
 * ```tsx
 * <ComponentName requiredProp="value" variant="primary">
 *   Content
 * </ComponentName>
 * ```
 */
export function ComponentName({
  requiredProp,
  optionalProp = 0,
  variant = DEFAULT_VARIANT,
  size = DEFAULT_SIZE,
  disabled = false,
  onClick,
  children,
  className,
}: ComponentNameProps): React.ReactElement {
  // --------------------------------------------------------------------------
  // State
  // --------------------------------------------------------------------------
  const [internalState, setInternalState] = useState(false);

  // --------------------------------------------------------------------------
  // Derived / Memoized Values
  // --------------------------------------------------------------------------
  const classNames = useMemo(
    () => getClassNames(variant, size, disabled, className),
    [variant, size, disabled, className]
  );

  const computedValue = useMemo(() => {
    // Expensive computation
    return optionalProp * 2;
  }, [optionalProp]);

  // --------------------------------------------------------------------------
  // Handlers
  // --------------------------------------------------------------------------
  const handleClick = useCallback(() => {
    if (disabled) return;

    setInternalState((prev) => !prev);
    onClick?.();
  }, [disabled, onClick]);

  // --------------------------------------------------------------------------
  // Render
  // --------------------------------------------------------------------------
  return (
    <div
      className={classNames}
      onClick={handleClick}
      role="button"
      tabIndex={disabled ? -1 : 0}
      aria-disabled={disabled}
    >
      {/* Header section */}
      <div className="component-name__header">
        <span>{requiredProp}</span>
        {computedValue > 0 && <span>({computedValue})</span>}
      </div>

      {/* Content section */}
      {children && (
        <div className="component-name__content">
          {children}
        </div>
      )}

      {/* State indicator (example) */}
      {internalState && (
        <div className="component-name__indicator">Active</div>
      )}
    </div>
  );
}

// ============================================================================
// Sub-components (for compound component pattern)
// ============================================================================

interface HeaderProps {
  children: React.ReactNode;
}

function Header({ children }: HeaderProps): React.ReactElement {
  return <div className="component-name__header">{children}</div>;
}

interface BodyProps {
  children: React.ReactNode;
}

function Body({ children }: BodyProps): React.ReactElement {
  return <div className="component-name__body">{children}</div>;
}

// Attach sub-components
ComponentName.Header = Header;
ComponentName.Body = Body;

// ============================================================================
// Default Export
// ============================================================================

export default ComponentName;

// ============================================================================
// USAGE EXAMPLES (remove in actual component)
// ============================================================================

/*
// Basic usage
<ComponentName requiredProp="Hello" />

// With all props
<ComponentName
  requiredProp="Hello"
  optionalProp={5}
  variant="secondary"
  size="lg"
  disabled={false}
  onClick={() => console.log('clicked')}
  className="custom-class"
>
  <p>Child content</p>
</ComponentName>

// Compound component usage
<ComponentName requiredProp="Compound">
  <ComponentName.Header>Header Content</ComponentName.Header>
  <ComponentName.Body>Body Content</ComponentName.Body>
</ComponentName>
*/
