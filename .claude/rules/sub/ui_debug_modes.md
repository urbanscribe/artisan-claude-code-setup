# UI Debug Modes Sub-Rule (Tier 3)
## Purpose
Defines debug mode patterns and environment-gated debug features for UI development and troubleshooting.

## DEBUG MODE ARCHITECTURE

### Environment-Based Gating
**STRICT ENVIRONMENT CHECKS**:
```javascript
// ❌ INCORRECT - Debug always visible
<div className="debug-panel">
  <h3>Debug Information</h3>
  <pre>{JSON.stringify(props, null, 2)}</pre>
</div>

// ✅ CORRECT - Environment-gated
{process.env.NODE_ENV === 'development' && (
  <div className="debug-panel">
    <h3>Debug Information</h3>
    <pre>{JSON.stringify(props, null, 2)}</pre>
  </div>
)}
```

**PYTHON/DJANGO EXAMPLE**:
```python
# settings.py
DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() == 'true'

# views.py
def debug_view(request):
    if not settings.DEBUG:
        raise Http404("Debug view not available in production")

    # Debug logic here
    context = {
        'database_queries': connection.queries,
        'cache_stats': cache.get_stats(),
        'user_permissions': request.user.get_all_permissions(),
    }
    return render(request, 'debug/debug_panel.html', context)
```

### Debug Feature Categories
**DEVELOPMENT-ONLY FEATURES**:
- **Data Visualization**: JSON dumps, state inspectors
- **Performance Metrics**: Render times, query counts
- **Error Boundaries**: Detailed error information
- **API Call Logging**: Request/response inspection
- **Component Boundaries**: Visual layout debugging

## DEBUG IMPLEMENTATION PATTERNS

### React Debug Components
**CONDITIONAL DEBUG RENDERING**:
```jsx
// components/DebugPanel.jsx
import React from 'react';

const DebugPanel = ({ data, title = 'Debug Data' }) => {
  // Strict environment check
  if (process.env.NODE_ENV !== 'development') {
    return null;
  }

  return (
    <div
      style={{
        position: 'fixed',
        top: '10px',
        right: '10px',
        background: 'rgba(0, 0, 0, 0.8)',
        color: 'white',
        padding: '10px',
        borderRadius: '5px',
        maxWidth: '400px',
        maxHeight: '300px',
        overflow: 'auto',
        zIndex: 9999,
        fontSize: '12px'
      }}
    >
      <h4>{title}</h4>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default DebugPanel;

// Usage in components
import DebugPanel from './DebugPanel';

const UserProfile = ({ user, loading, error }) => {
  const debugData = {
    user,
    loading,
    error,
    timestamp: new Date().toISOString(),
    renderCount: useRef(0).current++
  };

  return (
    <div>
      {/* Main component JSX */}
      <DebugPanel data={debugData} title="UserProfile Debug" />
    </div>
  );
};
```

### Vue Debug Directives
**CONDITIONAL DEBUG DIRECTIVES**:
```vue
<template>
  <div>
    <UserProfile v-if="user" :user="user" />

    <!-- Debug panel - only in development -->
    <div v-if="isDevelopment" class="debug-panel">
      <h4>Vue Debug Info</h4>
      <pre>{{ debugData }}</pre>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    isDevelopment() {
      return process.env.NODE_ENV === 'development';
    },
    debugData() {
      return {
        user: this.user,
        route: this.$route,
        store: this.$store.state,
        timestamp: new Date().toISOString()
      };
    }
  }
};
</script>

<style scoped>
.debug-panel {
  position: fixed;
  bottom: 10px;
  left: 10px;
  background: rgba(255, 255, 0, 0.9);
  border: 2px solid red;
  padding: 10px;
  max-width: 500px;
  max-height: 400px;
  overflow: auto;
  z-index: 10000;
}
</style>
```

### Angular Debug Services
**DEBUG SERVICE PATTERN**:
```typescript
// debug.service.ts
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DebugService {
  private isDevelopment = false;

  constructor() {
    this.isDevelopment = !environment.production;
  }

  log(component: string, data: any): void {
    if (this.isDevelopment) {
      console.group(`🔍 ${component} Debug`);
      console.log('Data:', data);
      console.log('Timestamp:', new Date().toISOString());
      console.log('Call Stack:', new Error().stack);
      console.groupEnd();
    }
  }

  showPanel(data: any, title = 'Debug Panel'): void {
    if (this.isDevelopment) {
      // Create and show debug panel
      const panel = document.createElement('div');
      panel.innerHTML = `
        <div style="
          position: fixed;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          background: white;
          border: 3px solid red;
          padding: 20px;
          z-index: 10001;
          max-width: 600px;
          max-height: 500px;
          overflow: auto;
        ">
          <h3>${title}</h3>
          <pre>${JSON.stringify(data, null, 2)}</pre>
          <button onclick="this.parentElement.remove()">Close</button>
        </div>
      `;
      document.body.appendChild(panel);
    }
  }
}

// Usage in components
import { DebugService } from './debug.service';

@Component({...})
export class UserComponent {
  constructor(private debugService: DebugService) {}

  ngOnInit() {
    this.debugService.log('UserComponent', {
      user: this.user,
      permissions: this.permissions,
      apiCalls: this.apiCallCount
    });
  }

  showDebugPanel() {
    this.debugService.showPanel({
      component: 'UserComponent',
      state: this.getState(),
      props: this.getProps()
    });
  }
}
```

## DEBUG ACCORDION PATTERNS

### Collapsible Debug Panels
**NON-INTRUSIVE DEBUGGING**:
```jsx
// components/DebugAccordion.jsx
import React, { useState } from 'react';

const DebugAccordion = ({ title, data, initiallyOpen = false }) => {
  const [isOpen, setIsOpen] = useState(
    process.env.NODE_ENV === 'development' ? initiallyOpen : false
  );

  // Don't render anything in production
  if (process.env.NODE_ENV !== 'development') {
    return null;
  }

  return (
    <details
      open={isOpen}
      style={{
        border: '1px solid #ccc',
        borderRadius: '4px',
        margin: '10px 0',
        background: '#f9f9f9'
      }}
    >
      <summary
        onClick={() => setIsOpen(!isOpen)}
        style={{
          padding: '8px 12px',
          cursor: 'pointer',
          fontWeight: 'bold',
          background: '#e9e9e9'
        }}
      >
        🔍 {title}
      </summary>
      <div style={{ padding: '12px' }}>
        <pre style={{
          background: 'white',
          padding: '10px',
          borderRadius: '4px',
          fontSize: '12px',
          overflow: 'auto',
          maxHeight: '300px'
        }}>
          {JSON.stringify(data, null, 2)}
        </pre>
      </div>
    </details>
  );
};

// Usage
<DebugAccordion
  title="API Response Debug"
  data={{
    response,
    loading,
    error,
    requestTime: Date.now()
  }}
  initiallyOpen={false}
/>
```

## DEBUG KEYBOARD SHORTCUTS

### Global Debug Toggle
**KEYBOARD-ACTIVATED DEBUGGING**:
```javascript
// debug-keyboard.js - Global debug keyboard shortcuts
if (typeof window !== 'undefined' && process.env.NODE_ENV === 'development') {
  let debugVisible = false;

  const toggleDebug = () => {
    debugVisible = !debugVisible;
    document.body.classList.toggle('debug-visible', debugVisible);

    // Dispatch custom event for components to listen to
    window.dispatchEvent(new CustomEvent('debug-toggle', {
      detail: { visible: debugVisible }
    }));
  };

  // Ctrl+Shift+D to toggle debug mode
  document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.shiftKey && e.key === 'D') {
      e.preventDefault();
      toggleDebug();
    }
  });

  // Ctrl+Shift+L to show performance metrics
  document.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.shiftKey && e.key === 'L') {
      e.preventDefault();
      console.table({
        'DOM Nodes': document.getElementsByTagName('*').length,
        'Event Listeners': performance.getEntriesByType('navigation')[0].loadEventEnd,
        'Memory Usage': (performance as any).memory,
        'Render Time': performance.now()
      });
    }
  });
}
```

## DEBUG LOGGING PATTERNS

### Structured Debug Logging
**DEVELOPMENT-ONLY LOGGING**:
```javascript
// debug-logger.js
const DEBUG_LOGGER = {
  log: (component, message, data = {}) => {
    if (process.env.NODE_ENV !== 'development') return;

    const timestamp = new Date().toISOString();
    const logEntry = {
      timestamp,
      component,
      message,
      data,
      stack: new Error().stack.split('\n').slice(2, 5) // First few stack frames
    };

    console.group(`🔍 ${component}: ${message}`);
    console.log('Data:', data);
    console.log('Timestamp:', timestamp);
    console.log('Stack:', logEntry.stack);
    console.groupEnd();

    // Store in localStorage for inspection
    const logs = JSON.parse(localStorage.getItem('debug_logs') || '[]');
    logs.push(logEntry);
    localStorage.setItem('debug_logs', JSON.stringify(logs.slice(-100))); // Keep last 100
  },

  showLogs: () => {
    if (process.env.NODE_ENV !== 'development') return;

    const logs = JSON.parse(localStorage.getItem('debug_logs') || '[]');
    console.table(logs);
  },

  clearLogs: () => {
    localStorage.removeItem('debug_logs');
  }
};

// Usage
import { DEBUG_LOGGER } from './debug-logger';

class ApiService {
  async fetchUser(id) {
    DEBUG_LOGGER.log('ApiService', 'Fetching user', { id });

    try {
      const response = await fetch(`/api/users/${id}`);
      const user = await response.json();

      DEBUG_LOGGER.log('ApiService', 'User fetched successfully', { id, user });
      return user;
    } catch (error) {
      DEBUG_LOGGER.log('ApiService', 'User fetch failed', { id, error: error.message });
      throw error;
    }
  }
}
```

## DEBUG BUILD CONFIGURATION

### Webpack Debug Configuration
**DEVELOPMENT BUILD ENHANCEMENTS**:
```javascript
// webpack.config.js
const isDevelopment = process.env.NODE_ENV === 'development';

module.exports = {
  mode: isDevelopment ? 'development' : 'production',
  devtool: isDevelopment ? 'eval-source-map' : 'source-map',

  plugins: [
    ...(isDevelopment ? [
      new webpack.DefinePlugin({
        __DEBUG__: JSON.stringify(true),
        __DEV__: JSON.stringify(true)
      })
    ] : [])
  ],

  optimization: {
    minimize: !isDevelopment,
    ...(isDevelopment && {
      usedExports: false, // Keep unused exports for debugging
    })
  }
};
```

### Environment Variable Patterns
**DEBUG FEATURE FLAGS**:
```bash
# .env.development
NODE_ENV=development
DEBUG_UI=true
DEBUG_API=true
DEBUG_PERFORMANCE=true
DEBUG_MEMORY=true

# Usage in code
const DEBUG_UI = process.env.DEBUG_UI === 'true';
const DEBUG_API = process.env.DEBUG_API === 'true';

if (DEBUG_UI) {
  // Render debug UI components
}

if (DEBUG_API) {
  // Log API calls and responses
}
```

## DEBUG TESTING PATTERNS

### Debug Feature Testing
**ENSURING DEBUG CODE DOESN'T LEAK**:
```javascript
// tests/debug.test.js
describe('Debug Features', () => {
  const originalEnv = process.env;

  beforeEach(() => {
    // Mock production environment
    process.env = { ...originalEnv, NODE_ENV: 'production' };
  });

  afterEach(() => {
    process.env = originalEnv;
  });

  test('debug panel does not render in production', () => {
    const { container } = render(<DebugPanel data={{ test: 'data' }} />);
    expect(container.firstChild).toBeNull();
  });

  test('debug logging is disabled in production', () => {
    const consoleSpy = jest.spyOn(console, 'log').mockImplementation();
    debugLogger.log('TestComponent', 'test message');

    expect(consoleSpy).not.toHaveBeenCalled();
    consoleSpy.mockRestore();
  });

  test('debug keyboard shortcuts are disabled in production', () => {
    // Mock production environment
    process.env.NODE_ENV = 'production';

    // Reload debug module to pick up environment change
    jest.resetModules();
    const debugKeyboard = require('./debug-keyboard');

    // Keyboard shortcuts should not be active
    expect(document.addEventListener).not.toHaveBeenCalled();
  });
});
```

## PRODUCTION CLEANUP PATTERNS

### Dead Code Elimination
**TREESHAKING DEBUG CODE**:
```javascript
// debug-utils.js
export const DEBUG_UTILS = process.env.NODE_ENV === 'development' ? {
  log: (component, message, data) => {
    console.group(`🔍 ${component}: ${message}`);
    console.log(data);
    console.groupEnd();
  },
  showPanel: (data) => {
    // Debug panel implementation
  }
} : {
  log: () => {}, // No-op in production
  showPanel: () => {} // No-op in production
};

// Usage - will be tree-shaken in production
import { DEBUG_UTILS } from './debug-utils';
DEBUG_UTILS.log('Component', 'Debug message', data);
```

### Build-Time Feature Flags
**COMPILE-TIME ELIMINATION**:
```javascript
// config.js
export const FEATURES = {
  DEBUG: process.env.NODE_ENV === 'development',
  ANALYTICS: true,
  CHAT: process.env.ENABLE_CHAT === 'true'
};

// webpack.config.js - DefinePlugin for compile-time elimination
new webpack.DefinePlugin({
  'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV),
  'FEATURES.DEBUG': JSON.stringify(process.env.NODE_ENV === 'development')
})

// Usage - completely eliminated in production builds
if (FEATURES.DEBUG) {
  console.log('This code is completely removed in production');
}
```

This comprehensive UI debug modes rule ensures debug features are strictly gated behind environment checks, provides multiple implementation patterns, and guarantees production safety through testing and build-time elimination. The patterns are designed to be non-intrusive during development while being completely invisible in production builds.```
</xai:function_call name="write">
<parameter name="file_path">claude_code/setup/.claude/rules/sub/arch_basics.md
