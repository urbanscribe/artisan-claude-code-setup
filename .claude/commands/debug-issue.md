description: Debug an issue using strategic logging and browser verification. argument-hint: [issue-description]
---------------------------------------------------------------------------------------------------------------

Debug Issue: $1
===============

Debug the following issue: $1

## Systematic Debugging Process

### 1. Enable Debug Mode
- Set .env DEBUG_UI=true for debug accordions
- Enable strategic logging at suspected failure points
- Prepare browser testing environment

### 2. Reproduce the Issue
- Clear reproduce steps with real data
- Check browser console for JavaScript errors
- Examine server logs for backend errors
- Verify database state and session handling

### 3. Isolate the Problem
- Use debug accordions to trace data flow
- Check API responses and DTO structures
- Verify async operation completion
- Test with minimal data sets

### 4. Apply Fix
- Make surgical code changes only
- Update or add tests as needed
- Verify fix with browser testing
- Check logs confirm proper execution

### 5. Validation
- Run full test suite
- Browser verification of fix
- Check for no regressions
- Disable debug mode when complete

## Debug Tools Available
- Browser debug accordions (.env DEBUG_UI=true)
- Strategic logging at key points
- Database session verification
- API response inspection

Document findings and fix applied.
