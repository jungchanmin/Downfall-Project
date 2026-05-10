# 🛠️ 1인 개발자를 위한 AI 도구 활용 튜토리얼 (v1.0)

> **대상**: AI 도구 초보자, 1인 개발 환경, *다운폴* 같은 텍스트·일러스트·음향 중심 게임 제작.
>
> **약속**: 본 가이드는 *어떤 버튼을 누르는가* 가 아니라, *어떤 워크플로로 사고하는가* 를 다룬다. 버튼은 변하지만 워크플로는 오래간다.

---

## 0. 마인드셋: AI 도구를 쓰는 5가지 원칙

1. **AI는 직원이 아니라 인턴이다**. 출력은 항상 검수 후 사용. 자존심 없이 *"다시 해"* 를 자주 말한다.
2. **컨텍스트가 곧 품질이다**. 좋은 입력 없이 좋은 출력 없다. 위키와 PRD를 *항상* AI에게 함께 준다.
3. **재현성을 확보한다**. 좋은 결과가 나왔을 때 *프롬프트·시드·설정* 을 즉시 저장한다.
4. **AI 의존 함정을 경계한다**. 매주 한 번은 *AI 없이* 자기 코드를 읽는다. 이해 못 하는 코드는 부채다.
5. **파이프라인 단위로 자동화한다**. 같은 작업을 3번째 시킨다면, 그건 *템플릿·스크립트로 묶어야 할 신호* 다.

---

## 🎨 PART 1 — 비주얼 디자인 (NovelAI)

### 1-1. NovelAI를 다운폴에 쓰는 이유
- 캐릭터 일러스트 일관성에 강함 (V4 기반, 캐릭터 슬롯 / vibe transfer)
- 어두운·문학적·19세기풍·심리적 분위기에 학습 친화적
- 데이터셋 라이선스가 비교적 명확
- 비용이 합리적 (월 정액)

### 1-2. 다운폴이 NovelAI에서 만들어야 할 자산 분류
| 카테고리 | 분량 | 톤 키워드 |
|---|---|---|
| 캐릭터 초상 (12명 × 표정 4종) | ~48장 | 흑백/세피아, 19세기 사진관, 무표정·신경증 |
| 장소 일러스트 (15구역 × 페이즈 변형 2) | ~30장 | 안개, 좁은 시야각, 인공적 정렬 |
| 이벤트 스팟 일러스트 (특수 이벤트만) | ~30장 | 비대칭 위협보다 *대칭의 불쾌감* |
| UI 장식 (장식틀, 구분선, 아이콘) | ~20개 | 빅토리아 인쇄소, 오컬트 도해 |

### 1-3. 캐릭터 일관성 워크플로

**문제**: 같은 캐릭터를 4가지 표정으로 그릴 때 얼굴이 매번 달라진다.

**해법** (V4 기준):
1. **베이스 시드 락(seed lock)**: 한 캐릭터의 *결정적 시드* 를 한 번 잘 뽑은 뒤, 모든 변형에서 같은 시드를 재사용.
2. **캐릭터 프롬프트 카드**: 각 캐릭터마다 *고정 프롬프트* 를 작성해 둔다.
   ```
   가빈 — 표준 프롬프트:
   30대 남성, 검은 머리 단정한 사이드 파트, 은테 안경, 회색 리넨 셔츠,
   날카로운 턱선, 굳은 입꼬리, 미세하게 떨리는 동공,
   sepia toned, 19th century studio photograph, soft window light,
   neutral background, neurotic intellectual atmosphere
   ```
3. **표정 바리에이션**: 위 프롬프트 끝에만 *변형 슬롯* 추가.
   - `..., expression: subtle disdain` (평상시)
   - `..., expression: forced control, eye twitch` (스트레스 발현)
   - `..., expression: hollow stare` (광기 임계 직전)
   - `..., expression: closed eyes, calm` (휴식 시)
4. **Vibe Transfer**: 한 컷이 마음에 들면, 그 컷을 *vibe transfer* 입력으로 다음 변형에 동봉. 유사도 0.6~0.75 권장.
5. **결과는 항상 *프롬프트 + 시드* 와 함께 보관**. `assets/characters/Gavin/_meta.json` 에 모든 변형의 메타 적재.

### 1-4. 다운폴 톤을 위한 프롬프트 패턴

**좋은 패턴** (셜리 잭슨 톤):
- `unsettling stillness, geometric symmetry too perfect, cold light from one window`
- `ordinary objects arranged with unsettling precision, no visible threat`
- `mid-distance shot, slightly tilted, viewer feels unobserved but should not`

**피할 패턴** (다운폴이 아닌 호러):
- ❌ `gore, blood, monster, demon, scary face` — 노골적 호러는 *일상의 배신* 필러를 위반
- ❌ `dramatic lighting, action pose, epic` — 캐릭터를 영웅화하지 않는다
- ❌ `bright colors, vibrant` — 채도 자체를 낮춘다

### 1-5. 후처리 (Photopea / GIMP / Photoshop)
NovelAI 출력은 *원료* 다. 게임에 들어가기 전 반드시:
1. **컬러 그레이딩 통일**: 다운폴은 *세피아 + 청회색 그림자* 의 두 톤. 모든 자산을 같은 그레이딩 스크립트에 통과.
2. **배경 분리**: 알파 컷아웃 후 게임 내 배경에 합성.
3. **그레인/노이즈**: 약한 필름 그레인을 일관 두께로 추가 → 톤 일체감.
4. **해상도 표준화**: 캐릭터 1024×1280 / 장소 1920×1080 / 아이콘 256×256.

### 1-6. 흔한 함정과 대응
| 함정 | 증상 | 대응 |
|---|---|---|
| 손가락 이상 | 6개 손가락, 비틀린 손목 | 캐릭터 컷 대부분을 *흉상(머리~가슴)* 으로 한정 |
| 대칭 깨짐 | 양 눈 크기 다름 | 인페인트로 한쪽만 재생성 |
| 톤 표류 | 작업 누적 후 옛 컷과 비교 시 색감 다름 | *기준 5장* 을 항상 모니터에 띄워두고 비교 |
| IP 누설 | 의도치 않게 알려진 캐릭터를 닮음 | 부정 프롬프트에 유명 IP 키워드 차단 |

### 1-7. 1주차 실습 미니 과제
- 가빈 / 레이첼 각 4표정 = 8장 완성
- 오뱅마을 *성당* 1장 (낮 / 밤 변형)
- UI 장식틀 1세트
- 메타 JSON 작성

---

## 💻 PART 2 — 코딩 (Claude Code / Google Antigravity)

### 2-1. 도구 비교 (2026년 5월 시점 기준 일반 가이드)
| 도구 | 강점 | 약점 | 다운폴 적합성 |
|---|---|---|---|
| **Claude Code** (CLI / IDE) | 대형 컨텍스트, 위키 같은 자료 동봉이 자연스러움, 멀티파일 리팩토링 견고 | 시각적 IDE 경험은 별도 IDE 통합으로 보충 | ⭐⭐⭐⭐⭐ |
| **Google Antigravity** | 에이전트 워크플로, 시각적 결과 미리보기 | 신규 도구라 패턴 정립 중 | ⭐⭐⭐⭐ |

→ **권장 1차 선택: Claude Code**. 위키 + PRD + 이벤트 JSON을 한 번에 컨텍스트로 넣고 작업할 때 가장 안정적.
→ Antigravity는 UI/시각 검증 단계(M5)에서 보조로 도입.

### 2-2. 프로젝트 구조 (Godot 4 기준)
```
/downfall
  /addons              # 외부 플러그인
  /scenes              # .tscn 씬
    main_loop.tscn
    event_modal.tscn
    character_card.tscn
  /scripts             # GDScript
    /core
      game_controller.gd
      turn_manager.gd
      event_director.gd
      memory_graph.gd
    /domain
      character.gd
      resource_pool.gd
      event.gd
    /data
      json_loader.gd
      save_system.gd
  /data                # 게임 데이터 (런타임 로드)
    /events/*.json
    /characters/*.json
  /assets
    /characters
    /locations
    /ui
    /audio
  /tools               # 빌드/QA 스크립트 (파이썬)
    lint_event.py
    extract_payload.py
    flag_graph.py
  /wiki                # 본 위키 (배포 시 제외)
  project.godot
```

### 2-3. AI 코딩 도구 사용 워크플로 (5단계)

**Step 1 — 컨텍스트 부팅**
세션 시작 시 AI에게 다음을 *반드시* 동봉:
- `ConText_Manifest.md`
- `03_Downfall_PRD.md`
- 작업 대상 영역의 기존 코드 파일들
- 작업할 데이터 샘플 (이벤트 JSON 1개 등)

**Step 2 — 사양을 글로 합의**
바로 코딩 시키지 않는다. 먼저:
> "이벤트 트리거 평가 엔진을 구현하기 전에, 입출력 / 함수 시그니처 / 엣지 케이스를 먼저 정의해줘. 코드는 아직 쓰지 마."

→ AI가 정리한 사양에 디렉터가 OK 한 다음에만 코드 단계로.

**Step 3 — 작은 단위로 생성**
한 번에 한 *책임* 만 시킨다.
- ❌ "이벤트 시스템 전체 만들어줘"
- ⭕ "Event 도메인 클래스만 만들어줘. 트리거 평가는 다음 단계에서."

**Step 4 — 즉시 테스트**
생성된 코드는 즉시 *유닛 테스트* 와 함께 묶는다. AI에게 같이 시킬 수 있다:
> "방금 만든 trigger evaluator의 GUT (Godot Unit Test) 케이스 6개 작성해줘. happy path, 빈 조건, 다중 조건 AND, OR 등."

**Step 5 — 자기 이해 점검**
*AI가 만든 코드를 다른 AI 세션에 던지지 말고, 직접 읽는다*. 30분 내에 그 파일을 *AI 없이* 다시 설명할 수 있다면 OK. 없다면 — 더 작게 쪼개서 다시.

### 2-4. AI에게 다운폴 컨텍스트를 *효율적으로* 주는 방법

**위키 한꺼번에 던지지 마라.** 컨텍스트 토큰이 낭비된다.

권장 패턴:
- **세션 1 (시스템 작업)**: PRD + Manifest + 해당 시스템 코드만
- **세션 2 (이벤트 작업)**: Manifest + 캐릭터 로어 바이블 1~2개 + 이벤트 템플릿 + 기존 이벤트 샘플 3~5개
- **세션 3 (디버깅)**: 에러 로그 + 관련 파일 2~3개만

각 세션이 시작할 때 *목적 한 줄* 을 명시:
> "이 세션의 목표는 X 시스템의 Y 함수를 구현·테스트하는 것이다."

### 2-5. Git & 버전 관리 (필수)

1인 개발이라도 git은 *세이브 슬롯* 이다.
- 매일 작업 시작 시 새 브랜치 (`feature/event-trigger-eval`)
- AI가 만든 변경은 *작은 커밋 단위로 분리*
- 커밋 메시지에 *왜* 를 적는다 (무엇은 diff가 보여줌)
- 매주 일요일에 일주일치 브랜치를 정리해 main에 머지

### 2-6. 흔한 함정과 대응
| 함정 | 증상 | 대응 |
|---|---|---|
| 환각 API | 존재하지 않는 함수 호출 | 컴파일/런타임 에러를 그대로 다시 던져서 수정 시킴 |
| 거대한 Diff | 한 변경이 수백 라인 | 단위 작게 잘라서 다시 시킴 — 거대 패치는 *받지 않음* |
| 보수적 거절 | "이건 위험할 수 있습니다" | 사양에 더 구체적으로 명시 후 재요청 |
| 스타일 표류 | 같은 프로젝트 내 코딩 스타일이 파일마다 다름 | `STYLE.md` 를 만들어 매 세션 동봉 |

### 2-7. 1주차 실습 미니 과제
- Godot 프로젝트 부팅 + 메인 루프 씬
- `Character` 도메인 클래스 + 단위 테스트
- 이벤트 JSON 1개를 로드해서 콘솔에 본문 출력
- git 저장소 초기화 + 첫 5커밋

---

## 🎵 PART 3 — 음악 (AI 작곡)

### 3-1. 추천 도구
| 도구 | 강점 | 다운폴 적합성 |
|---|---|---|
| **Suno** | 가창·구조 있는 트랙에 강함 | 엔딩 보컬, 광기 발현 트랙용 |
| **Udio** | 기악·앰비언트에 강함 | 페이즈 BGM의 핵심 도구 |
| **AIVA** | 클래식·정통 작법 | 시네마틱 엔딩에 |
| **ElevenLabs Sound Effects** | 효과음 생성 | 일상의 배신용 미세한 SFX |

→ **1차 조합: Udio (BGM) + ElevenLabs (SFX) + Suno (특수 트랙 1~2개)**

### 3-2. 다운폴이 만들어야 할 음향 자산
| 카테고리 | 분량 | 길이 | 비고 |
|---|---|---|---|
| 페이즈 BGM (5종 × 변형 3) | 15곡 | 2~3분 루프 | 새벽/아침/점심/저녁/밤 + 평화/긴장/위기 |
| 이벤트 스팅거 | 20개 | 5~10초 | 트랙 A 발현, 트랙 B 결과 발현용 |
| 보스/엔딩 트랙 | 6~8개 | 3~5분 | 각 엔딩 분기당 1개 |
| 앰비언트 레이어 | 10개 | 30초 루프 | 장소별 배경 |
| SFX | ~50개 | 짧음 | 발걸음, 문, 종이, 미세한 어긋남용 SFX |

### 3-3. 다운폴 톤을 위한 프롬프트 패턴 (Udio 기준)

**페이즈 BGM 예시 — 새벽:**
```
sparse strings sustain in low register, distant church bell every 16 bars,
field recording of cold wind under the strings, key of D minor barely tonal,
no percussion, dynamic always pp to mp,
victorian funeral ambience, haunted but not supernatural,
3 minutes, seamless loop, no climax
```

**페이즈 BGM 예시 — 밤 (긴장):**
```
single piano note clusters in mid register, irregular interval (2-7 seconds apart),
wood creaks recorded close, almost subliminal female humming,
no melody, no chord progression, drifting and hypnotic,
shirley jackson the haunting of hill house atmosphere,
2 min loop, ends back where it began
```

**스팅거 예시 — 통제 강박 발현:**
```
8 seconds, single low piano cluster sustained,
metallic ruler tap on glass at 2s, 4s, 5.5s, 7s — slightly inconsistent,
final tap is half a beat early — wrong on purpose,
no resolution
```

### 3-4. *일상의 배신* 을 음향으로 구현하기

다운폴의 음향 시그니처는 다음 3가지 원칙:
1. **빈 공간(silence)을 두려워하지 않는다**. 음악이 *있는 것* 보다 *없는 것* 이 더 무섭다.
2. **온음계의 미세 이탈**. 트랙 끝의 한 음만 미세하게 어긋난다 (반음 절반).
3. **반복의 무너짐**. 4번 반복되는 패턴이 5번째에 0.5박자 어긋난다 — 의식적으로.

이 3원칙을 위반하는 트랙은 *기각*. 셜리 잭슨 4지침의 음향 버전이라고 본다.

### 3-5. 후처리 (Audacity / Reaper)
1. **루프 포인트 처리**: 모든 BGM은 *seamless loop* 가 되어야 함. 시작점·끝점 매칭 + 짧은 크로스페이드.
2. **러프니스 정상화**: LUFS -18 ~ -20 선에서 통일. 게임 내 페이즈 전환 시 볼륨 점프 방지.
3. **레이어링 슬롯**: BGM은 항상 *2~3 레이어* 로 분리 출력 (베이스 / 멜로딕 / 앰비언트). 인게임에서 긴장도에 따라 레이어를 켜고 끔.
4. **포맷**: OGG Vorbis (게임 친화), 음원 원본은 WAV로 따로 보관.

### 3-6. 라이선스 / 권리 관리
- 사용 도구의 *상업적 이용 가능 플랜* 인지 매번 확인
- 생성 트랙의 *프롬프트·시드·도구·플랜* 을 `assets/audio/_credits.json` 에 기록
- 가창이 들어가는 트랙은 추가 위험 — 가능하면 기악으로

### 3-7. 흔한 함정과 대응
| 함정 | 증상 | 대응 |
|---|---|---|
| 너무 영화적 | 곡 자체는 좋지만 *주연이 됨* | "background, no melody, ambient" 강하게 |
| 클라이맥스 강요 | AI가 곡 끝에 항상 빌드업 | "never resolves, no climax, ends quietly" |
| 장르 표류 | 곡마다 분위기 다름 | *레퍼런스 트랙 3개* 를 정해두고 매 프롬프트에 인용 |
| 길이 문제 | 너무 짧거나 늘어짐 | 후처리에서 잘라서 루프 포인트 재구성 |

### 3-8. 1주차 실습 미니 과제
- 새벽 BGM 1곡 (3분 루프)
- 밤(긴장) BGM 1곡 (2분 루프)
- 이벤트 스팅거 5종
- SFX 10종 (문, 발걸음, 종이, 시계, 미세 어긋남)

---

## 🔄 PART 4 — 통합 워크플로 (3 도구를 하나의 파이프라인으로)

### 4-1. 한 이벤트가 만들어지기까지 (예시)

```
1. 디렉터: 위키 데이터 → Claude Code 컨베이어 벨트로 이벤트 텍스트 양산
   → /Wiki/05_Events/EVT_B007_a1f3.md
2. QA Gate A·B 통과 → JSON 변환
   → /data/events/EVT_B007_a1f3.json
3. 이벤트가 시각 컷을 요구하면 → NovelAI로 이벤트 스팟 일러스트
   → /assets/events/EVT_B007_a1f3.png
4. 이벤트가 특수 음향을 요구하면 → Udio로 스팅거
   → /assets/audio/stingers/EVT_B007_a1f3.ogg
5. Claude Code: 이벤트 모달 씬에 신규 이벤트 로드 테스트
6. 결과를 디렉터가 인게임에서 1회 트리거 → OK / 회송
```

### 4-2. 주간 운영 리듬 (1인 풀타임 가정)

| 요일 | 모드 | 산출물 |
|---|---|---|
| 월 | 디렉터 모드 | 이번 주 만들 이벤트 키워드 / 캐릭터 / 장소 정의 |
| 화 | 작가 모드 (Claude Code) | 이벤트 텍스트 양산 + Gate B 검수 |
| 수 | 엔지니어 모드 (Claude Code) | Gate C 검수 + 시스템 코드 작업 |
| 목 | 비주얼 모드 (NovelAI) | 이번 주 자산 일러스트 |
| 금 | 음향 모드 (Udio) | 이번 주 음향 자산 |
| 토 | 통합 빌드 | 전부 합쳐서 인게임 동작 확인 |
| 일 | 회고 + 휴식 | 다음 주 계획 / 휴식 |

→ **모드 분리가 가장 중요하다.** 같은 날에 작가/엔지니어를 동시에 하면 둘 다 흐려진다.

### 4-3. 자산 폴더 표준
모든 AI 자산은 *재현 메타데이터* 를 동봉.
```
/assets/characters/Gavin/portrait_v3.png
/assets/characters/Gavin/portrait_v3.meta.json   # 프롬프트, 시드, 도구, 날짜
```

→ 6개월 뒤에 같은 컷을 *다시* 만들 수 있어야 한다.

### 4-4. AI 의존 함정 방지 체크리스트 (매주 자가 점검)
- [ ] 이번 주 작성한 코드 중 *내가 직접 설명 못 하는* 파일이 있는가? → 다음 주에 재학습
- [ ] 이번 주 만든 이벤트 중 *셜리 잭슨 톤* 이 약한 게 있는가? → 회송
- [ ] 이번 주 만든 자산 중 *재현 메타데이터가 빠진* 것이 있는가? → 즉시 보강
- [ ] 이번 주, *AI 없이* 작업한 시간이 0이었는가? → 다음 주는 의도적으로 시간 확보

---

## 5. 학습 곡선 로드맵 (입문자 → 운용자)

| 주차 | 목표 |
|---|---|
| 1주차 | 각 도구의 *1주차 실습 미니 과제* 완수 |
| 2~4주차 | 같은 도구로 양산 — 캐릭터 12명 / 장소 15개 / BGM 5곡 |
| 5~8주차 | 통합 워크플로 첫 사이클 — 이벤트 1개를 텍스트~비주얼~음향~코드까지 풀 통합 |
| 9~16주차 | 사이클 반복으로 콘텐츠 풀 빌드 |
| 17주차 이후 | 빌드/배포·QA 자동화·플레이테스트 |

---

## 6. 위기 시 대응 매뉴얼

### 6-1. 막혔을 때
- 30분 같은 문제 → AI에게 *문제만* 다시 설명 (해결책 강요 X)
- 1시간 같은 문제 → 휴식 → 종이에 손으로 그림
- 반나절 같은 문제 → 다른 작업으로 전환, 다음 날 신선한 머리로

### 6-2. AI가 망친 작업이 누적될 때
- 즉시 *오늘의 변경 전부* 를 git revert
- 무엇이 망가졌는지 *메모* 만 남기고, 그날은 더 작업하지 않는다

### 6-3. 톤이 흔들린다고 느낄 때
- *원본 셜리 잭슨* 을 30분 읽는다
- `ConText_Manifest.md` 의 라이팅 지침을 다시 정독
- 최근 만든 산출물 5개를 *기준 5개* 와 비교

---

## 7. 마무리

> AI 도구는 *당신의 안목을 대체하지 않는다*. 단지 안목이 결정한 것을 더 빨리 실행하게 도와줄 뿐이다.
>
> 다운폴은 톤의 게임이다. 톤의 마지막 책임자는 *사람* 이다.
> 도구를 신뢰하되, 결정은 양보하지 말 것.

---

**관련 문서**: `01_AI_Event_Pipeline_Roadmap.md`, `02_Event_QA_Protocol.md`, `03_Downfall_PRD.md`
