# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-11-09

### Added

- `greet()`: `punctuation` 인수를 추가하여 고정된 느낌표 대신 문장 부호를 지정할 수 있도록 개선.

### Fixed

- `greet()`: 빈 문자열이나 공백 이름 시 빈 인사말(`Hello, !`) 대신 `world`(`Hello, world!`)를 사용하도록 수정.

## [0.1.0] - 2026-11-09

### Added

- `greet()`: 이름을 받아 인사말을 반환하는 함수 및 명령행 인터페이스 추가.
