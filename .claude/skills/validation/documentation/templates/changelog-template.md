# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New features that have been added

### Changed
- Changes in existing functionality

### Deprecated
- Features that will be removed in upcoming releases

### Removed
- Features that have been removed

### Fixed
- Bug fixes

### Security
- Security vulnerability fixes

---

## [1.2.0] - 2024-01-15

### Added
- User profile customization options (#123)
- Support for dark mode across all pages
- New `/api/v2/users` endpoint with enhanced filtering
- Bulk import feature for resources

### Changed
- Updated authentication flow to support MFA
- Improved error messages for validation failures
- Migrated from Express to Fastify for better performance

### Deprecated
- `/api/v1/users` endpoint (use `/api/v2/users` instead)
- `legacyAuth` configuration option

### Fixed
- Fixed race condition in concurrent user updates (#456)
- Resolved memory leak in WebSocket connections
- Fixed timezone handling in date filters

### Security
- Updated bcrypt to v5.1.0 to address CVE-2024-XXXXX
- Added rate limiting to authentication endpoints

---

## [1.1.0] - 2024-01-01

### Added
- Webhook support for real-time event notifications
- Export functionality for user data (CSV, JSON)
- Two-factor authentication option

### Changed
- Improved dashboard loading performance by 40%
- Updated to Node.js 20 LTS
- Redesigned settings page for better UX

### Fixed
- Fixed pagination issue when filtering by date range
- Corrected email template encoding for special characters

---

## [1.0.1] - 2023-12-15

### Fixed
- Hot fix for login redirect loop
- Fixed missing translations in error messages

### Security
- Patched XSS vulnerability in user input fields

---

## [1.0.0] - 2023-12-01

### Added
- Initial release
- User authentication and authorization
- Resource CRUD operations
- RESTful API with OpenAPI documentation
- Admin dashboard
- Email notifications
- Basic reporting

---

## Version Guidelines

### Version Format: MAJOR.MINOR.PATCH

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality (backwards compatible)
- **PATCH**: Bug fixes (backwards compatible)

### When to Update Each Section

#### Added
- New features
- New API endpoints
- New configuration options
- New CLI commands

#### Changed
- Updates to existing features
- UI/UX improvements
- Performance improvements
- Dependency updates

#### Deprecated
- Features planned for removal
- Old API versions
- Legacy configuration options

#### Removed
- Deleted features
- Removed API endpoints
- Removed configuration options

#### Fixed
- Bug fixes
- Typo corrections
- Documentation fixes

#### Security
- Security patches
- Vulnerability fixes
- Security improvements

---

## Links

[Unreleased]: https://github.com/username/project/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/username/project/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/username/project/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/username/project/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/username/project/releases/tag/v1.0.0
