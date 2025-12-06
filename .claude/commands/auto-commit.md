name: auto-commit
version: "1.0"
last_updated: "2025-03-22"
description: "git diffの内容から自動的にコミットメッセージを生成し、コミットを実行"

concept: |
  自動コミットモードは、現在のワーキングディレクトリの変更内容を分析し、
  適切なコミットメッセージを自動生成して、即座にコミットを実行するモードです。
  煩雑なコミットメッセージ作成の手間を削減しながら、
  プロジェクトの慣例に従った品質の高いコミットを実現します。

trigger:
  command: "/auto-commit"
  options:
    - name: scope
      description: "コミットのスコープを明示的に指定"
      example: "/auto-commit --scope commands"
    - name: type
      description: "命令タイプを強制指定"
      example: "/auto-commit --type fix"
    - name: no-verify
      description: "pre-commit hooksをスキップ（非推奨）"
      example: "/auto-commit --no-verify"
    - name: amend
      description: "最後のコミットを修正（危険：直前コミットのみ対応）"
      example: "/auto-commit --amend"

typical_use_cases:
  - "今の変更をサッとコミットしたい"
  - "git diffから自動でいい感じのメッセージを作ってほしい"
  - "毎回メッセージを考えるのが手間"
  - "章を書き終わったからコミットしたい"
  - "複数のモードファイルを更新したからコミットしたい"

message_generation:
  analysis_targets:
    - "変更ファイル - どのファイルが変更されたか"
    - "変更内容 - git diffから実質的な変更を抽出"
    - "プロジェクト文脈 - Chapters/, .claude/commands/ など"
    - "変更の性質 - 新規追加、修正、更新など"

  command_types:
    - name: Add
      description: "新しいファイル・機能の追加"
    - name: Update
      description: "既存ファイルの更新・改善"
    - name: Fix
      description: "バグ修正・誤字修正"
    - name: Refactor
      description: "構造の再編成"
    - name: Docs
      description: "ドキュメント更新"
    - name: Remove
      description: "ファイル・コンテンツの削除"
    - name: Move
      description: "ファイルの移動・リネーム"

  priority_rules:
    - "新規ファイル追加 → Add 命令"
    - "大幅な変更(>50行) → Update 命令"
    - "小さな修正(<10行) → Fix または Refactor"
    - "削除 → Remove 命令"
    - "複数ファイル混在 → 最も影響度の高い命令を選択"

message_format: |
  [命令] [対象] - [簡潔な説明]

  [詳細説明があれば]

  🤖 Generated with Auto-Commit Mode
  Co-Authored-By: Claude <noreply@anthropic.com>

execution_flow:
  step_1: "分析: git status と git diff を読む"
  step_2: "メッセージ生成: 分析結果に基づいて、最適なメッセージを生成"
  step_3: "ステージング: git add で変更ファイルを自動ステージング"
  step_4: "コミット: 生成メッセージでコミット実行、完了メッセージを表示"

safety_mechanisms:
  pre_commit_confirmation: false
  auto_execution: true
  execution_detail: |
    - ユーザー確認なしで自動実行
    - git status と git diff を分析して自動でメッセージ生成
    - 変更ファイルを自動でステージングしてコミット実行
    - コミット完了後、その結果をレポート表示

  warnings:
    - "Large number of files changed (12 files以上) → 警告メッセージを表示"
    - "Deleting multiple files → 削除内容の確認メッセージを表示"

best_practices:
  recommended:
    - "小さな、関連性のある変更セット に使用"
    - "章の完成時、コマンド実装時 など、単位が明確な時"
    - "定期的な整理・更新"
  avoid:
    - "大規模で無関係な変更の混在"
    - "本来別々の作業を同時に実行"
    - "秘密情報（パスワード、APIキーなど）を含む変更"

related_modes:
  - "/task-focus - タスク完了後のコミット"
  - "/reflection - 1日の作業をコミット前に振り返る"
