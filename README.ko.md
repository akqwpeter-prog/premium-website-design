# Premium Website Design

[English](README.md) · [中文版](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Français](README.fr.md)

개인 사이트, 포트폴리오, 랜딩 페이지를 방향 설정부터 디자인 토큰, 타이포그래피, 인터랙션, 생성 아트, 라이트/다크 테마, QA, 배포까지 일관되게 설계하는 Codex 스킬입니다.

**이 스킬로 만든 예시:** https://mengjin-site.pages.dev

## 기능

1. **디자인 리드** - 대상과 요구를 파악하고 변주/모션/밀도 다이얼 설정
2. **방향** - 하나의 명확한 미학에 집중, 템플릿 느낌 제거
3. **토큰과 골격** - OKLCH 다크퍼스트 테마 + 라이트 테마
4. **인터랙션** - 캐릭터 등장, 스포트라이트, 3D 틸트, 마그넷 버튼, 스크롤 연동, 마퀴, 테마 전환
5. **아트워크** - 시드 기반 생성 아트(API 키 불필요), AI 아바타(프라이버시 포함)
6. **아이콘** - Iconify / Simple Icons / iconfont 자동 검색·다운로드 + 검증 체크리스트
7. **검증과 배포** - 프리플라이트, Playwright QA, Cloudflare Pages

## 설치

Codex에서 이 저장소의 스킬 설치를 요청하거나 스킬 디렉터리에 복사합니다.

```bash
cp -r premium-website-design ~/.codex/skills/
```

## 구성

```text
SKILL.md                      핵심 워크플로
references/preflight.md       릴리스 체크리스트
references/interactions.md    모션 구현
references/art-pipeline.md    생성 아트 + 아바타 + 프라이버시
references/icons.md           아이콘 획득 + 검증
assets/tokens.css             디자인 토큰
scripts/qa_site.py            Playwright QA
```

## 라이선스

MIT
